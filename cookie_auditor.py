import argparse,json,re
from pathlib import Path
def audit(line):
 low=line.lower()
 return {"httponly":"httponly" in low,"secure":"secure" in low,"samesite":bool(re.search(r"samesite=(lax|strict|none)",low)),"name":line.split("=",1)[0].strip()}
def main():
 p=argparse.ArgumentParser();p.add_argument("file");x=p.parse_args()
 rows=[audit(s.strip()) for s in Path(x.file).read_text(encoding="utf-8").splitlines() if s.strip() and "=" in s]
 print(json.dumps(rows,indent=2))
if __name__=="__main__":main()
