"use client";

import { TrendingUp } from "lucide-react";
import {
  Label,
  PolarGrid,
  PolarRadiusAxis,
  RadialBar,
  RadialBarChart,
  ResponsiveContainer, // Import ResponsiveContainer
} from "recharts";

import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import { ChartConfig, ChartContainer } from "@/components/ui/chart";
import useDependabilityStore from "@/store/dependabilitystore";

interface DependabilityData {
  phase: string;
  value: number;
}

export function ScoreChart() {
  const baseEquipmentDependability: DependabilityData[] = [
    { phase: "Harbour", value: 0.739496314 },
    { phase: "Cruise", value: 0.708115973 },
    { phase: "Action", value: 0.818549922 },
  ];

  const randomizeValue = (value: number) => {
    const randomPercentage = (Math.random() - 0.5) * 0.4; // Random value between -0.2 and 0.2
    return value + value * randomPercentage;
  };

  const equipmentDependability = baseEquipmentDependability.map((dep) => ({
    ...dep,
    value: randomizeValue(dep.value),
  }));

  const calculateEuclideanDistance = (values: number[]) => {
    const idealVector = [1, 1, 1];
    let sum = 0;
    for (let i = 0; i < values.length; i++) {
      sum += Math.pow(values[i] - idealVector[i], 2);
    }
    return Math.sqrt(sum);
  };

  const values = equipmentDependability.map((dep) => dep.value);
  const euclideanDistance = calculateEuclideanDistance(values);
  const calculatedValue = Math.round(((1.73 - euclideanDistance) / 1.73) * 100); // Round to nearest whole number

  const chartData = [
    {
      name: "background",
      value: 100,
      fill: "rgba(255, 255, 255, 0.1)",
    },
    {
      name: "score",
      value: calculatedValue, // Use the rounded value
      fill: "#E8FF40",
    },
  ];

  const chartConfig = {
    value: {
      label: "Score",
    },
  } satisfies ChartConfig;

  return (
    <Card className="text-gray-200 flex flex-col h-2/3 rounded-lg backdrop-blur-md bg-white/10 p-6 shadow-2xl border border-white/20">
      <CardHeader className="items-center pb-2">
        <CardTitle className="text-white text-2xl font-bold tracking-wide">
          Dependability Score
        </CardTitle>
        <CardDescription className="text-gray-400 text-sm">
          System Level Dependability
        </CardDescription>
      </CardHeader>
      <CardContent className="flex-1 pb-0">
        <ChartContainer
          config={chartConfig}
          className="mx-auto aspect-square max-h-[250px]"
        >
          {/* Wrap RadialBarChart in ResponsiveContainer */}
          <ResponsiveContainer width="100%" height="100%">
            <RadialBarChart
              data={chartData}
              startAngle={90}
              endAngle={-270}
              innerRadius={80}
              outerRadius={110}
            >
              <PolarGrid gridType="circle" radialLines={false} stroke="none" />
              <RadialBar
                dataKey="value"
                maxBarSize={100}
                cornerRadius={10}
                background={false}
              />
              <PolarRadiusAxis tick={false} tickLine={false} axisLine={false}>
                <Label
                  content={({ viewBox }) => {
                    if (viewBox && "cx" in viewBox && "cy" in viewBox) {
                      return (
                        <text
                          x={viewBox.cx}
                          y={viewBox.cy}
                          textAnchor="middle"
                          dominantBaseline="middle"
                        >
                          <tspan
                            x={viewBox.cx}
                            y={viewBox.cy}
                            className="fill-white text-5xl font-extrabold drop-shadow-lg"
                          >
                            {chartData[1].value}% {/* Use chartData[1].value */}
                          </tspan>
                          <tspan
                            x={viewBox.cx}
                            y={(viewBox.cy || 0) + 28}
                            className="fill-gray-300 text-sm font-medium tracking-wide"
                          >
                            Dependability Score
                          </tspan>
                        </text>
                      );
                    }
                  }}
                />
              </PolarRadiusAxis>
            </RadialBarChart>
          </ResponsiveContainer>
        </ChartContainer>
      </CardContent>
      {equipmentDependability.map((dep, index) => (
        <CardFooter key={index} className="flex-col gap-2 text-sm">
          <Card className="w-1/2 text-lg  tracking-wide uppercase text-gray-200 flex flex-row items-center gap-2 justify-between px-4 py-3 text-left font-semibold rounded-lg backdrop-blur-md bg-white/10 shadow-2xl border border-white/20 max-w-3xl">
            <div className="">{dep.phase}: </div>
            <div>{dep.value.toFixed(2)}</div>
          </Card>
        </CardFooter>
      ))}
    </Card>
  );
}
