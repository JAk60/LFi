"use client"
import { useState, useEffect } from "react";
import { motion, AnimatePresence } from "framer-motion";

export default function ChayanTextEffect() {
  const [isEnglish, setIsEnglish] = useState(true);

  useEffect(() => {
    const interval = setInterval(() => {
      setIsEnglish((prev) => !prev);
    }, 10000); // Toggle every 10 seconds
    return () => clearInterval(interval);
  }, []);

  return (
    <div className="flex justify-center items-center h-screen bg-gray-900 text-white text-4xl font-bold">
      <AnimatePresence mode="wait">
        <motion.div
          key={isEnglish ? "english" : "hindi"}
          initial={{ opacity: 0, rotateY: 90 }}
          animate={{ opacity: 1, rotateY: 0 }}
          exit={{ opacity: 0, rotateY: -90 }}
          transition={{ duration: 1 }}
          className="text-6xl"
        >
          {isEnglish ? "Chayan" : "चयन"}
        </motion.div>
      </AnimatePresence>
    </div>
  );
}
