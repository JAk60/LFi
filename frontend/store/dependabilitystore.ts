import { create } from 'zustand';

interface DependabilityStore {
  systemDependability: number;
  equipmentDependability: number[];
  
  // Single unified setter that matches your data format
  setDependabilityData: (data: { 
    system_dependability: number; 
    equipment_dependability: number[] 
  }) => void;
}

const useDependabilityStore = create<DependabilityStore>((set) => ({
  systemDependability: 0,
  equipmentDependability: [0, 0, 0],
  
  setDependabilityData: (data) => set({
    systemDependability: data.system_dependability,
    equipmentDependability: data.equipment_dependability,
  }),
}));

export default useDependabilityStore;