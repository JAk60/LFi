"use client";
import { Button } from "@/components/ui/button";
import {
  MessageSquare,
  Users,
  Library,
  FolderClosed,
  MessageCircle,
} from "lucide-react";
import Image from "next/image";
import hiveicon from "./cell.png";
import dynamic from "next/dynamic";
import Link from "next/link";
import { useEffect, useState } from "react";
import useSentenceStore from "@/store/TextStore";
import { useRouter } from "next/navigation";

const MotionDiv = dynamic(
  () => import("framer-motion").then((mod) => mod.motion.div),
  { ssr: false }
);

interface Paragraph {
  ParagraphID: number;
  ParagraphText: string;
  ParaCreatedDate: string;
}

export function Sidebar() {
  const { setSentence, setRecentChats } = useSentenceStore();
  const [textArray, setTextArray] = useState<string[]>([]);
  const router = useRouter();

  useEffect(() => {
    async function fetchData() {
      try {
        const response = await fetch("http://127.0.0.1:8000/paragraphs/");
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data: Paragraph[] = await response.json();
        const texts: string[] = data.map((item) => item.ParagraphText);
        setTextArray(texts);
        setRecentChats(texts); // Store in Zustand for global access
      } catch (error) {
        console.error("Error fetching paragraphs:", error);
      }
    }

    fetchData();
  }, [setRecentChats]);

  const handleChatClick = (chat: string) => {
    router.push("/"); // Navigate to homepage
    setSentence(chat); // Set the selected chat in the store
  };

  const handleNewChat = () => {
    setSentence(""); // Clear the sentence in the store
    router.push("/");
  };

  return (
    <div className="h-screen mr-[15rem]">
      <div className="h-screen w-64 fixed border-r flex flex-col bg-black/80 rounded-md backdrop-filter backdrop-blur-sm">
        <Link href="/">
          <div className="flex items-center p-4">
            <MotionDiv
              animate={{ rotate: [0, 360] }}
              transition={{
                repeat: Infinity,
                duration: 1.5,
                repeatDelay: 8.5,
                ease: "easeInOut",
              }}
            >
              <Image
                priority
                src={hiveicon}
                alt="Hive Icon"
                height={70}
                width={100}
                className="p-4"
              />
            </MotionDiv>
            <h1 className="font-[Amita] text-5xl text-white">चयन</h1>
          </div>
        </Link>
        <div className="p-4">
          <Button
            variant="outline"
            className="bg-[#FAE500] w-full justify-start gap-2 text-black border-gray-800"
            onClick={handleNewChat}
          >
            <MessageSquare className="h-4 w-4" />
            New Chat
          </Button>
        </div>

        <div className="mt-6">
          <h3 className="px-4 text-xs font-semibold text-gray-400 mb-2">
            Recent Chats
          </h3>
          <div className="overflow-y-auto space-y-1 px-2">
            {textArray.length > 0 ? (
              textArray.map((chat, index) => {
                const truncatedText =
                  chat.split(" ").slice(0, 4).join(" ") +
                  (chat.split(" ").length > 4 ? "..." : "");
                return (
                  <Button
                    key={index}
                    variant="ghost"
                    className="overflow-hidden whitespace-nowrap text-ellipsis flex-1 py-2 px-3 cursor-pointer flex w-full justify-start text-sm text-gray-400 truncate"
                    onClick={() => handleChatClick(chat)}
                  >
                    {truncatedText}
                  </Button>
                );
              })
            ) : (
              <p className="text-gray-500 text-sm text-center">
                No recent chats
              </p>
            )}
          </div>
        </div>
      </div>
    </div>
  );
}
