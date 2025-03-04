"use client"
import { motion } from "framer-motion";
import React from "react";

const HexagonLoader = () => {
  const hexagons = Array.from({ length: 19 });

  return (
    <div className="flex justify-center items-center h-screen bg-black">
      <div className="relative w-40 h-40 flex flex-wrap justify-center items-center">
        {hexagons.map((_, index) => (
          <motion.div
            key={index}
            className="absolute w-6 h-6 bg-cyan-400"
            style={{
              clipPath: "polygon(50% 0%, 100% 25%, 100% 75%, 50% 100%, 0% 75%, 0% 25%)",
              transform: `rotate(${(index * 360) / hexagons.length}deg)`,
            }}
            animate={{
              scale: [1, 1.2, 1],
              opacity: [1, 0.5, 1],
            }}
            transition={{
              duration: 1.5,
              repeat: Infinity,
              ease: "easeInOut",
              delay: index * 0.1,
            }}
          />
        ))}
      </div>
    </div>
  );
};

export default HexagonLoader;