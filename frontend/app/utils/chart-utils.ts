import { ChartDataPoint } from "../types/data";

// utils/chart-utils.ts
export const transformToChartData = (data: Record<string, number>): ChartDataPoint[] => {
    return Object.entries(data).map(([name, value]) => ({
      name,
      value: Number((value * 100).toFixed(1))
    }));
  };
  
  