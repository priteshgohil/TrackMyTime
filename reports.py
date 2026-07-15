def fmt(s):
 s=int(s); return f"{s//3600:02}:{(s%3600)//60:02}:{s%60:02}"
def build_report(rows):
 lines=["Daily Report",""]
 for d,a,i,l in rows[:7]: lines.append(f"{d} A:{fmt(a)} I:{fmt(i)} L:{fmt(l)}")
 lines.append("")
 lines.append(f"Monthly Active: {fmt(sum(r[1] for r in rows))}")
 return "\n".join(lines)
