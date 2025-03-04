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
import Link from "next/link";

export function Sidebar() {
  const recentChats = [
    "React form error handlin...",
    "Next js invitation card...",
    "Custom Ask v0 text area...",
    "Create NEXY JS Project...",
    "Custom Form Submission...",
    "Create sidebar links",
    "Async fetch error",
    "Using form with categori...",
    "Checkbox console log",
    "Typescript table compone...",
  ];
  const handlef = () => {
    console.log("boom");
  };
  return (
    <div className="relative w-64 border-r border-gray-800 flex flex-col">
      <div className="flex justify-start items-center">
        <Image
          priority
          src={hiveicon}
          alt="Follow us on Twitter"
          height={70}
          width={100}
          className="p-4 transition-transform duration-300 hover:rotate-180"
        />
        <Link href={"/"}>
          <span className="text-3xl">चयन</span>
        </Link>
      </div>
      <div className="p-4">
        <Button
          onClick={handlef}
          variant="outline"
          className="bg-[#FAE500] w-full justify-start gap-2 text-black border-gray-800"
        >
          <MessageSquare className="h-4 w-4" />
          New Chat
        </Button>
      </div>

      <nav className="space-y-1 px-2">
        {[
          { icon: Users, text: "Community" },
          { icon: Library, text: "Library" },
          { icon: FolderClosed, text: "Projects" },
          { icon: MessageCircle, text: "Feedback" },
        ].map(({ icon: Icon, text }) => (
          <Button
            key={text}
            variant="ghost"
            className="w-full justify-start gap-2 text-gray-400"
          >
            <Icon className="h-4 w-4" />
            {text}
          </Button>
        ))}
      </nav>

      <div className="mt-6">
        <h3 className="px-4 text-xs font-semibold text-gray-400 mb-2">
          Recent Chats
        </h3>
        <div className="space-y-1 px-2">
          {recentChats.map((chat) => (
            <Button
              key={chat}
              variant="ghost"
              className="w-full justify-start text-sm text-gray-400 truncate"
            >
              {chat}
            </Button>
          ))}
        </div>
      </div>

      <div className="mt-auto p-4">
        <div className="rounded bg-gray-900 p-4 text-sm">
          <h4 className="font-semibold mb-2">New Feature</h4>
          <p className="text-gray-400">
            v0 will now expose its reasoning in responses.
          </p>
        </div>
      </div>
    </div>
  );
}
