import json,os,urllib.request as U
TP=dict(P="----.//+.,+----1../2//137777----",N="#%''%)-.'./0'-01'.01'-/0%)--#%''",B=")++++.--+///+-//+../+-./+---)+++",R="-"*32,Q=")++,+-.-+...--..,-..+-..+---)++,",K="13/-11--+))))''%'%%#'%%#'%%#'%%#'%%#")
V=dict(P=100,N=300,B=320,R=500,Q=950,K=0)
EV={}
for p,t in TP.items():
 e=[0]*120
 for q in range(64):e[91-q//8*10+q%8]=V[p]+ord(t[q//8*4+min(q%8,7-q%8)])*5-225
 EV[p]=e
D=dict(N=(-21,-19,-12,-8,8,12,19,21),B=(-11,-9,9,11),R=(-10,-1,1,10))
D["Q"]=D["K"]=D["B"]+D["R"]
MATE,CAP=10**5,40000
nd=[0]
TT={}
H=set()
r=lambda i:110-i+2*(i%10)
def R(b,s,w,e,k,x):
 f="".join(b[q-10:q]for q in range(120,0,-10)).swapcase()
 return f,-s,(w&3)*4|(w>>2),r(e),r(x),r(k)
def A(b,s):
 for ds,c in(((-9,-11),"p"),(D["N"],"n"),(D["Q"],"k")):
  for d in ds:
   if b[s+d]==c:return 1
 for n,d in enumerate(D["Q"]):
  j=s
  while b[j:=j+d]==".":0
  if b[j]in("bq","rq")[n>3]:return 1
 return 0
def G(b,w,e):
 for i,p in enumerate(b):
  if not p.isupper():continue
  if p=="P":
   for d in(-10,-9,-11):
    j=i+d
    if d==-10:
     if b[j]!=".":continue
    elif not(b[j].islower()or j==e):continue
    if j<30:
     for pr in"QRBN":yield i,j,pr
    else:
     yield i,j,""
     if d==-10 and 80<i<89 and b[i-20]==".":yield i,i-20,""
  else:
   for d in D[p]:
    j=i
    while b[j:=j+d]!=" ":
     if b[j]=="."or b[j].islower():yield i,j,""
     if b[j]!="."or p in"NK":break
   if p=="K"and i==95:
    for bit,tg,pa,rf in((1,97,(96,97),98),(2,93,(94,93,92),91)):
     if w&bit and b[rf]=="R"and all(b[q]=="."for q in pa)and not A(b,95)+A(b,pa[0])+A(b,pa[1]):yield 95,tg,""
def M(pos,m):
 b,s,w,e,k,x=pos
 i,j,pr=m
 p,cap=b[i],b[j]
 n=list(b);n[i]=".";n[j]=pr or p
 s+=EV[p][j]-EV[p][i]
 if pr:s+=EV[pr][j]-EV[p][j]
 if cap!=".":s+=EV[cap.upper()][r(j)]
 ne=0
 if p=="P":
  if j==e and cap==".":
   n[j+10]=".";s+=EV["P"][r(j+10)]
  elif j==i-20:ne=i-10
 if p=="K":
  w&=12;k=j
  if abs(j-i)==2:
   f,t=(98,96)if j>i else(91,94)
   n[f]=".";n[t]="R";s+=EV["R"][t]-EV["R"][f]
 if p=="R":w&=15-2*(i==91)-(i==98)
 w&=15-8*(j==21)-4*(j==28)
 return R("".join(n),s,w,ne,k,x)
X=SystemExit
def N(pos,d,a,be,ply):
 nd[0]+=1
 if nd[0]>CAP:raise X
 b,s=pos[:2]
 w,e,k,x=pos[2:]
 if pos[0]in H and not ply&1:return 0
 if d<=0:
  if s>=be:return be
  a=max(a,s)
  ms=sorted([m for m in G(b,w,e)if b[m[1]].islower()],key=lambda m:-V[b[m[1]].upper()])
  for m in ms:
   if b[m[1]]=="k":return MATE-ply
   v=-N(M(pos,m),0,-be,-a,ply+1)
   if v>a:a=v
   if a>=be:break
  return a
 key=(b,w)
 en=TT.get(key)
 if en and en[0]>=d:
  if en[2]==0:return en[1]
  a=max(a,en[1])
  if a>=be:return en[1]
 ms=sorted(G(b,w,e),key=lambda m:-V[b[m[1]].upper()]*16+V[b[m[0]]]if b[m[1]].islower()else 0)
 best=-MATE-1
 a0=a
 for m in ms:
  if b[m[1]]=="k":return MATE-ply
  v=-N(M(pos,m),d-1,-be,-a,ply+1)
  if v>best:best=v
  if v>a:a=v
  if a>=be:break
 if best<=-MATE+ply+1:return-MATE+ply if A(b,k)else 0
 if best>a0:TT[key]=(d,best,0 if best<be else 1)
 return best
def F(fen):
 pt=fen.split()
 bd=[*" "*20,*" ........ "*8,*" "*20]
 s=0;i=21
 for c in pt[0]:
  if c=="/":i+=2
  elif c.isdigit():i+=int(c)
  else:
   bd[i]=c
   s+=EV[c][i]if c.isupper()else-EV[c.upper()][r(i)]
   i+=1
 b="".join(bd)
 w=0
 for c in"qkQK":w=w*2+(c in pt[2])
 pos=(b,s,w,0,b.index("K"),b.index("k"))
 fl=pt[1]=="b"
 if fl:pos=R(*pos)
 return pos,fl
def S(fen,legal):
 pos,fl=F(fen)
 H.add(pos[0])
 def u2(m):
  i,j,pr=m
  if fl:i,j=r(i),r(j)
  return f"{chr(i%10+96)}{10-i//10}{chr(j%10+96)}{10-j//10}{pr.lower()}"
 mv=[(m,u2(m))for m in G(pos[0],pos[2],pos[3])if u2(m)in legal]
 bu=mv[0][1]
 for d in range(31):
  nd[0]=0
  try:
   cu,a=None,-MATE-1
   for m,u in mv:
    v=-N(M(pos,m),d-1,-MATE,-a if a>-MATE else MATE,1)
    if v>a:a,cu=v,u
   bu=cu
   mv.sort(key=lambda t:t[1]!=bu)
  except X:break
 return bu
def post(p,b):
 return json.load(U.urlopen(U.Request(os.environ["MAKEFUN_ENV_URL"]+p,data=json.dumps(b).encode())))
while 1:
 g=post("/game",{})
 if g["status"][0]=="d":break
 H.clear()
 while g["status"][0]=="y":g=post("/move",{"game":g["game"],"move":S(g["fen"],g["legal_moves"])})
