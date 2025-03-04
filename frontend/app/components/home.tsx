"use client"
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { PaperclipIcon } from "lucide-react";
import { Sidebar } from "./sidebar";
import {
  Loader2,
  Send,
  Image,
  FileCode,
  Upload,
  Layout,
  UserPlus,
} from "lucide-react";
import { Textarea } from "@/components/ui/textarea";
import { useState } from "react";
import { askV0 } from "../actions/ask-v0";
import { useFormStatus } from "react-dom";
type PredictionCategory = Record<string, number>;
type Prediction = Record<string, PredictionCategory>;
// import { CommunityGrid } from "./community-grid";
function SubmitButton() {
  const { pending } = useFormStatus();

  return (
    <Button
      type="submit"
      disabled={pending}
      className="bg-[#FAE500] hover:bg-zinc-700 text-black"
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


export default function MAinPage() {
     const [predictions, setPredictions] = useState<any | null>(null);
      const [error, setError] = useState<string | null>(null);
    
      async function handleSubmit(event: React.FormEvent<HTMLFormElement>) {
        event.preventDefault();
        const formData = new FormData(event.currentTarget);
    
        try {
          const result = await askV0(formData);
          if (result && "predictions" in result) {
            setPredictions(result.predictions);
            setError(null);
          } else if (result && "error" in result) {
            console.error(result.error);
            setError(result.error);
            setPredictions(null);
          }
        } catch (err) {
          console.error(err);
          setError("An unexpected error occurred.");
          setPredictions(null);
        }
      }
  return (
    <div className="flex h-screen bg-black text-white">
      <Sidebar />
      <main className="flex-1 flex items-center justify-center">
        <form
          onSubmit={handleSubmit}
          className=" space-y-4 rounded-xl p-[300px] bg-zinc-900/30 backdrop-blur-md bg-clip-padding border border-zinc-800/80"
        >
          <h1 className="text-4xl font-bold tracking-tight text-zinc-100 text-center mb-12">
            What can I help you ship?
          </h1>

          <Textarea
            name="scenario"
            placeholder="Please enter your mission statement..."
            className="min-h-[100px] w-full bg-zinc-900/40 border-zinc-800/50 text-zinc-100 placeholder:text-zinc-500 rounded-xl transition-all duration-200 focus:border-zinc-700 focus:ring-zinc-700 focus:min-h-[100px]"
          />

          <div className="flex flex-wrap gap-2">
            {[
              { icon: Image, text: "Clone a Screenshot" },
              { icon: FileCode, text: "Import from Figma" },
              { icon: Upload, text: "Upload a Project" },
              { icon: Layout, text: "Landing Page" },
              { icon: UserPlus, text: "Sign Up Form" },
            ].map(({ icon: Icon, text }) => (
              <Button
                key={text}
                variant="outline"
                type="button"
                className="bg-zinc-900/40 text-zinc-300 border-zinc-800/50 hover:bg-zinc-800/60 transition-colors"
              >
                <Icon className="w-4 h-4 mr-2" />
                {text}
              </Button>
            ))}
          </div>

          <div className="flex justify-end">
            <SubmitButton />
          </div>
        </form>
        {error && <p className="text-red-400 text-sm">{error}</p>}

        {predictions && (
          <div className="space-y-6 bg-zinc-900/50 rounded-xl p-6">
            <h3 className="text-xl font-semibold text-zinc-100">
              Predictions:
            </h3>

            <div className="space-y-6">
              {/* Predclass Output */}
              <div>
                <h4 className="text-lg font-medium text-zinc-200 mb-3">
                  Predclass Output:
                </h4>
                {predictions.predclass_output &&
                  Object.entries(predictions.predclass_output).map(
                    ([category, values], index) =>
                      renderCategoryOutput(category, values)
                  )}
              </div>

              {/* LFapplier Output */}
              <div>
                <h4 className="text-lg font-medium text-zinc-200 mb-3">
                  LFapplier Output:
                </h4>
                {predictions.LFapplier_output &&
                  Object.entries(predictions.LFapplier_output).map(
                    ([category, values], index) =>
                      renderCategoryOutput(category, values)
                  )}
              </div>
            </div>
          </div>
        )}
      </main>
    </div>
  );
}
  const renderCategoryOutput = (
    category: string,
    values: PredictionCategory
  ) => {
    return (
      <div key={category} className="mb-4 bg-black/10 rounded-lg p-4">
        <h4 className="text-md font-semibold capitalize text-zinc-200">
          {category}:
        </h4>
        <ul className="space-y-1">
          {Object.entries(values).map(([key, value], index) => (
            <li key={index} className="flex justify-between text-zinc-300">
              <span className="capitalize">{key}:</span>
              <span>{(value * 100).toFixed(2)}%</span>
            </li>
          ))}
        </ul>
      </div>
    );
  };
