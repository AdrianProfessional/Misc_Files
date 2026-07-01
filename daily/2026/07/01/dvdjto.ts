// Auto-generated TypeScript module

interface Fvbme {
  id: string;
  value: number;
  label: string;
  active: boolean;
}

export function validate(items: Fvbme[]): Fvbme[] {
  return items.filter(item => item.active).sort((a, b) => a.value - b.value);
}

export function run(items: Fvbme[]): Fvbme[] {
  return items.filter(item => item.active).sort((a, b) => a.value - b.value);
}
