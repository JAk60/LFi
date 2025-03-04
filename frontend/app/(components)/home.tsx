"use client";
import { Button } from "@/components/ui/button";
import { Textarea } from "@/components/ui/textarea";
import useModelStore from "@/store/ModelOutput";
import { Loader2, Send } from "lucide-react";
import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";
import { User, useUserStore } from "@/store/UserStore";
import { useFormStatus } from "react-dom";
import { askV0 } from "../actions/ask-v0";
import useSentenceStore from "@/store/TextStore";
import { get_dependability } from "../actions/dep";

function SubmitButton() {
  const { pending } = useFormStatus();

  return (
    <Button
      type="submit"
      disabled={pending}
      className="z-11 bg-[#FAE500] hover:bg-zinc-700 text-black"
    >
      {pending ? (
        <>
          <Loader2 className="mr-2 h-4 w-4 animate-spin" />
          Predicting...
        </>
      ) : (
        <>
          <Send className="mr-2 h-4 w-4" />
          Get Predictions
        </>
      )}
    </Button>
  );
}

export default function MainPage({ user }: User) {
  const { setUser } = useUserStore();
  const { sentence, setSentence } = useSentenceStore();
  const [textareaValue, setTextareaValue] = useState("");

  const router = useRouter();
  const [userRole, setUserRole] = useState<string | null>(null);
  const [error, setError] = useState<string | null>(null);
  const { setL1Data, setL2Data } = useModelStore();

  // Set user and fetch role from localStorage in useEffect
  useEffect(() => {
    setUser(user);

    // Check if window is defined (ensures code runs only on the client)
    if (typeof window !== "undefined") {
      const role = localStorage.getItem("user-role");
      setUserRole(role);
      console.log("User Role from localStorage:", role);
    }
  }, [user, setUser]);

  // Update textarea value when sentence changes in the store
  useEffect(() => {
    setTextareaValue(sentence);
  }, [sentence]);

  const handleTextareaChange = (e: React.ChangeEvent<HTMLTextAreaElement>) => {
    setTextareaValue(e.target.value);
  };

  async function handleSubmit(event: React.FormEvent<HTMLFormElement>) {
    event.preventDefault();
    const formData = new FormData(event.currentTarget);
    const text = formData.get("scenario") as string;
    setSentence(text);

    if (userRole === "Expert" || userRole === "Trainer") {
      try {
        const result = await askV0(formData);
        console.log(result);
        if (result && "predictions" in result) {
          setL1Data(result.predictions.predclass_output);
          setL2Data(result.predictions.LFapplier_output);
          setError(null);
          router.push(
            userRole === "Expert" || userRole === "Trainer"
              ? "/dashboard"
              : "/result"
          );
        }
      } catch (err) {
        console.error(err);
        setError("An unexpected error occurred.");
      }
    } else if (userRole === "User") {
      try {
        const result = await get_dependability();
        router.push("/result");
        console.log(result);
      } catch (err) {
        console.error(err);
        setError("An unexpected error occurred.");
      }
    }
  }

  return (
    <main className="z-10 flex-1 flex items-center justify-center">
      <form
        onSubmit={handleSubmit}
        className="w-3/4 space-y-4 rounded-xl p-[300px] bg-zinc-900/30 bg-clip-padding border border-zinc-800/80"
      >
        <h1 className="flex items-center justify-center gap-6 text-5xl font-bold tracking-tight text-zinc-100 text-center mb-12">
          <span>Welcome to</span>
          <span className="!font-[Amita] text-5xl text-white whitespace-nowrap">
            चयन
          </span>
          <span className="text-white">,</span>
          <span>{user.role}</span>
        </h1>

        <Textarea
          name="scenario"
          placeholder="Please enter your mission statement..."
          className="backdrop-blur-sm min-h-[100px] w-full bg-zinc-800/40 border-zinc-800/50 text-zinc-100 placeholder:text-zinc-500 rounded-xl transition-all duration-200 focus:border-zinc-700 focus:ring-zinc-700 focus:min-h-[100px]"
          value={textareaValue}
          onChange={handleTextareaChange}
        />

        <div className="relative flex justify-end">
          <SubmitButton />
        </div>
      </form>
      {error && <p className="text-red-400 text-sm">{error}</p>}
    </main>
  );
}
