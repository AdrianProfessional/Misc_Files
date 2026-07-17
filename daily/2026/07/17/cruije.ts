// Auto-generated TypeScript module

interface Gzvil {
  id: string;
  value: number;
  label: string;
  active: boolean;
}

export function run(items: Gzvil[]): Gzvil[] {
  return items.filter(item => item.active).sort((a, b) => a.value - b.value);
}

export function parse(items: Gzvil[]): Gzvil[] {
  return items.filter(item => item.active).sort((a, b) => a.value - b.value);
}
