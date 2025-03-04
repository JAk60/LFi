"use client";

import { motion } from "framer-motion";
import { useState, useEffect } from "react";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";


interface GaugeProps {
  value: number; // Percentage (0-100)
  label: string;
}

export default function Gauge({ value, label }: GaugeProps) {
  const [progress, setProgress] = useState(0);

  useEffect(() => {
    setTimeout(() => setProgress(value), 300); // Smooth transition
  }, [value]);

  return (
    <Card className="bg-white/10 border border-white/20 backdrop-blur-lg shadow-lg rounded-2xl p-4 w-64 h-64 flex flex-col items-center justify-center">
      <CardHeader className="text-center">
        <CardTitle className="text-white text-lg font-semibold">{label}</CardTitle>
      </CardHeader>
      <CardContent className="relative flex items-center justify-center">
        {/* Background Circle */}
        <svg className="absolute" width="140" height="140" viewBox="0 0 100 100">
          <circle
            cx="50"
            cy="50"
            r="40"
            stroke="rgba(255,255,255,0.2)"
            strokeWidth="8"
            fill="none"
          />
        </svg>
        {/* Animated Progress Circle */}
        <svg width="140" height="140" viewBox="0 0 100 100">
          <motion.circle
            cx="50"
            cy="50"
            r="40"
            stroke="#FFD700"
            strokeWidth="8"
            fill="none"
            strokeDasharray="251.2"
            strokeDashoffset={251.2 - (251.2 * progress) / 100}
            strokeLinecap="round"
            animate={{ strokeDashoffset: 251.2 - (251.2 * progress) / 100 }}
            transition={{ duration: 1, ease: "easeOut" }}
          />
        </svg>
        {/* Center Label */}
        <div className="absolute text-white text-3xl font-bold">
          {Math.round(progress)}%
        </div>
      </CardContent>
    </Card>
  );
}
