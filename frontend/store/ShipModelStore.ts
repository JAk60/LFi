// src/store/shipModelStore.ts
import { create } from 'zustand';

interface ShipModelState {
  selectedShipModel: string | null;
  setSelectedShipModel: (model: string) => void;
}

const useShipModelStore = create<ShipModelState>((set) => ({
  selectedShipModel: "ship1",
  setSelectedShipModel: (model) => set({ selectedShipModel: model }),
}));

export default useShipModelStore;
