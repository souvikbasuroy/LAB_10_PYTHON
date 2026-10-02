# Q7: Knowledge base using propositional logic (classroom domain)
# facts = true propositions; rules = (set of premises) -> conclusion (Horn clauses)

class KnowledgeBase:
    def __init__(self):
        self.facts = set()
        self.rules = []

    def add_fact(self, p):
        self.facts.add(p)

    def add_rule(self, premises, conclusion):
        self.rules.append((frozenset(premises), conclusion))

    def infer_all(self):
        """forward chaining: returns all provable propositions and the derivation steps"""
        known = set(self.facts)
        steps = []
        changed = True
        while changed:
            changed = False
            for prem, concl in self.rules:
                if concl not in known and prem <= known:
                    known.add(concl)
                    steps.append(f"{' & '.join(sorted(prem))} => {concl}")
                    changed = True
        return known, steps

    def ask(self, query):
        known, steps = self.infer_all()
        return query in known, steps

if __name__ == "__main__":
    kb = KnowledgeBase()
    # facts
    for f in ["TeacherPresent", "StudentsPresent", "ProjectorOn", "Daytime"]:
        kb.add_fact(f)
    # rules
    kb.add_rule(["TeacherPresent", "StudentsPresent"], "ClassInSession")
    kb.add_rule(["ClassInSession", "ProjectorOn"], "LectureRunning")
    kb.add_rule(["ClassInSession", "Daytime"], "LightsOff")        # (just a demo rule)
    kb.add_rule(["LectureRunning"], "StudentsListening")
    kb.add_rule(["StudentsListening", "TeacherPresent"], "LearningHappens")
    kb.add_rule(["ExamDay"], "SilenceRequired")

    print("Facts:", sorted(kb.facts))
    print("Rules:")
    for p, c in kb.rules:
        print("  ", " & ".join(sorted(p)), "->", c)

    for q in ["LectureRunning", "LearningHappens", "SilenceRequired", "ExamDay"]:
        ok, steps = kb.ask(q)
        print(f"\nQuery: {q}  ->  {'TRUE (entailed)' if ok else 'CANNOT BE INFERRED'}")
    print("\nDerivation steps:")
    for s in kb.ask("x")[1]:
        print("  ", s)

    # interactive
    while True:
        q = input("\nask a proposition (or 'quit'): ").strip()
        if q.lower() in ("quit", "q", ""): break
        print("TRUE" if kb.ask(q)[0] else "cannot be inferred")
