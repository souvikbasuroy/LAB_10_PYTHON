# Q8: Semantic network (vehicles) with IS-A, HAS-A, CAN and inheritance

class SemanticNetwork:
    def __init__(self):
        self.rel = {}   # node -> {"IS-A": set, "HAS-A": set, "CAN": set}

    def add(self, node, relation, target):
        self.rel.setdefault(node, {"IS-A": set(), "HAS-A": set(), "CAN": set()})
        self.rel[node][relation].add(target)

    def ancestors(self, node):
        out, stack = [], list(self.rel.get(node, {}).get("IS-A", []))
        while stack:
            n = stack.pop(0)
            if n not in out:
                out.append(n)
                stack.extend(self.rel.get(n, {}).get("IS-A", []))
        return out

    def properties(self, node, relation):
        """own + inherited properties through IS-A links"""
        res = set(self.rel.get(node, {}).get(relation, []))
        for a in self.ancestors(node):
            res |= self.rel.get(a, {}).get(relation, set())
        return res

    def is_a(self, node, target):
        return node == target or target in self.ancestors(node)

    def describe(self, node):
        if node not in self.rel:
            print(f"'{node}' not in knowledge base"); return
        print(f"\n{node}:")
        print("  IS-A  :", sorted(self.ancestors(node)) or "-")
        print("  HAS-A :", sorted(self.properties(node, "HAS-A")) or "-")
        print("  CAN   :", sorted(self.properties(node, "CAN")) or "-")

    def query(self, q):
        w = q.lower().replace("?", "").split()
        nodes = {n.lower(): n for n in self.rel}
        # "is car a vehicle" / "does car have engine" / "can car carry passengers"
        try:
            if w[0] == "is" and "a" in w:
                i = w.index("a"); a = nodes.get(" ".join(w[1:i])); b = nodes.get(" ".join(w[i+1:]))
                return f"{a} IS-A {b}: {self.is_a(a, b)}"
            if w[0] in ("does", "has") and "have" in w:
                i = w.index("have"); a = nodes.get(" ".join(w[1:i])); b = " ".join(w[i+1:])
                return f"{a} HAS-A {b}: {b in self.properties(a, 'HAS-A')}"
            if w[0] == "can":
                a = nodes.get(w[1]); b = " ".join(w[2:])
                return f"{a} CAN {b}: {b in self.properties(a, 'CAN')}"
            if w[0] == "describe" or w[0] == "what":
                self.describe(nodes.get(w[-1])); return ""
        except Exception:
            pass
        return "could not understand query"

if __name__ == "__main__":
    sn = SemanticNetwork()
    sn.add("Vehicle", "HAS-A", "wheels"); sn.add("Vehicle", "CAN", "move")
    sn.add("Car", "IS-A", "Vehicle"); sn.add("Car", "HAS-A", "engine"); sn.add("Car", "CAN", "carry passengers")
    sn.add("Bike", "IS-A", "Vehicle"); sn.add("Bike", "HAS-A", "pedals"); sn.add("Bike", "CAN", "be balanced")
    sn.add("SportsCar", "IS-A", "Car"); sn.add("SportsCar", "CAN", "go fast")
    sn.add("Truck", "IS-A", "Vehicle"); sn.add("Truck", "CAN", "carry cargo")
    sn.add("Airplane", "IS-A", "Vehicle"); sn.add("Airplane", "HAS-A", "wings"); sn.add("Airplane", "CAN", "fly")

    for n in ["SportsCar", "Bike", "Airplane"]:
        sn.describe(n)

    print("\nsample queries:")
    for q in ["is sportscar a vehicle", "does sportscar have wheels", "can sportscar carry passengers", "can bike fly"]:
        print(" ", q, "->", sn.query(q))

    print("\ninteractive (examples: 'is car a vehicle', 'can truck carry cargo', 'describe car', 'quit')")
    while True:
        q = input("query> ").strip()
        if q.lower() in ("quit", "q", ""): break
        r = sn.query(q)
        if r: print(r)
