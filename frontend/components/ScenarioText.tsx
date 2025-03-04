"use client";

import { Card, CardContent } from "@/components/ui/card";
import useSentenceStore from "@/store/TextStore";

export function SentenceDisplay() {
  const { sentence } = useSentenceStore();

  return (
    <Card className="h-full text-gray-200 flex flex-row items-center justify-center p-6 rounded-lg backdrop-blur-md bg-white/10 shadow-2xl border border-white/20 max-w-3xl">
      <p className="text-white text-2xl font-bold">
        {sentence || "No sentence stored"}
      </p>
    </Card>
  );
}

export default SentenceDisplay;
