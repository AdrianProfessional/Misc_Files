// Auto-generated TypeScript module

interface Rwbki {
  id: string;
  value: number;
  label: string;
  active: boolean;
}

export function fetch(items: Rwbki[]): Rwbki[] {
  return items.filter(item => item.active).sort((a, b) => a.value - b.value);
}

export function encode(items: Rwbki[]): Rwbki[] {
  return items.filter(item => item.active).sort((a, b) => a.value - b.value);
}
