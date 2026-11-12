import json as J,os as O,urllib.request as Q
V=(100,300,320,500,900,0)
B=100000
P='PNBRQK'
U=str.isupper;L=str.lower
T='j'*8+'t'*8+'llnppnllkkloolkkjjjnnjjjkihjjhikkllffllk'+'j'*8+'`bddddb`bfjjjjfbdjlmmljddkmnnmkddjmnnmjddklmmlkdbfjkkjfb`bddddb`'+'j'*64+'j'*64+'j'*64+'fhhiihhfhjjjjjjhhjkkkkjhijkkkkjijjkkkkjihkkkkkjhhjkjjjjhfhhiihhf'
K=(17,15,10,6,-6,-10,-15,-17)
D=(8,-8,1,-1,9,7,-7,-9)
def f(s):
 f=s.split();return list(''.join('.'*int(c) if c.isdigit() else c for c in f[0] if c!='/')),f[1]=='w',sum(1<<i for i in range(4) if 'KQkq'[i] in f[2]),-1 if f[3]=='-' else (8-int(f[3][1]))*8+ord(f[3][0])-97
def h(b,s,w):
 y,x=divmod(s,8);py=y+2*w-1
 if 0<=py<8 and any(0<=x+d<8 and b[py*8+x+d]==('P' if w else 'p')for d in(-1,1)):return 1
 if any(0<=s+d<64 and abs((s+d)%8-x)in(1,2)and b[s+d]==('N' if w else 'n')for d in K):return 1
 for d in D:
  for n in range(1,8):
   t=s+d*n
   if not 0<=t<64 or t%8-x!=n*(1 if d%8==1 else -1 if d%8==7 else 0):break
   c=b[t]
   if c!='.':
    p=L(c)
    if U(c)==w and(p=='q' or n==1 and p=='k' or p in 'rb' and(p=='r')==(abs(d)in(1,8))):return 1
    break
 return 0
def g(s):
 b,w,r,e=s
 for a,c in enumerate(b):
  if c=='.' or U(c)!=w:continue
  y,x=divmod(a,8);p=L(c)
  if p=='p':
   d=1-2*w;Y=y+d
   if 0<=Y<8:
    z='qn' if Y in(0,7)else('',);t=a+8*d
    if b[t]=='.':
     for q in z:yield a,t,q
     if y==1+5*w and b[t+8*d]=='.':yield a,t+8*d,''
    for X in(x-1,x+1):
     if 0<=X<8:
      t=Y*8+X
      if t==e or b[t]!='.' and U(b[t])!=w and L(b[t])!='k':
       for q in z:yield a,t,q
   continue
  ds=K if p=='n' else D[:4]if p=='r' else D[4:]if p=='b' else D
  for d in ds:
   for n in range(1,2 if p in 'nk' else 8):
    t=a+d*n
    if not 0<=t<64 or p=='n' and abs(t%8-x)!=3-abs(t//8-a//8) or p!='n' and t%8-x!=n*(1 if d%8==1 else -1 if d%8==7 else 0):break
    if b[t]=='.':yield a,t,''
    else:
     if U(b[t])!=w and L(b[t])!='k':yield a,t,''
     break
  if p=='k' and a==4+56*w and not h(b,a,not w):
   for d in 1,-1:
    bit=1<<(2*(not w)+(d<0))
    if r&bit and all(b[a+d*i]=='.' for i in range(1,3+(d<0)))and not h(b,a+d,not w):yield a,a+2*d,''
def m(s,m):
 b,w,r,e=s;b=b.copy();a,t,p=m;c=b[a];ep=L(c)=='p' and t==e and b[t]=='.' and a%8!=t%8;b[a]='.'
 if ep:b[t+(8 if w else-8)]='.'
 b[t]=p.upper()if p and w else p or c
 if L(c)=='k' and abs(t-a)==2:u=t+1 if t>a else t-2;v=t-1 if t>a else t+1;b[v]=b[u];b[u]='.'
 if L(c)=='k':r&=~(3 if w else 12)
 for q in(a,t):r&=~({63:1,56:2,7:4,0:8}.get(q,0))
 return b,not w,r,(a+t)//2 if L(c)=='p' and abs(t-a)==16 else-1
def l(s):
 w=s[1]
 return(q for q in g(s)if not h((b:=m(s,q)[0]),b.index('K' if w else 'k'),not w))
def v(s):
 b,w=s[:2];z=sum((1-2*c.islower())*(V[q]+5*(ord(T[q*64+(i if U(c)else i^56)])-106))for i,c in enumerate(b)if c!='.' for q in(P.index(c.upper()),))
 return z if w else-z
def r(s,m):
 b,w,r,e=s;a,t,_=m;c=b[t]if b[t]!='.' else 'p'
 return 10*V[P.index(c.upper())]-V[P.index(b[a].upper())]if b[t]!='.' or L(b[a])=='p' and t==e and a%8!=t%8 else-1
class C(Exception):pass
N=0;KL=[0]*512
def n(s,d,a,b,p):
 global N
 if N>5499:raise C
 N+=1;w=s[1];chk=h(s[0],s[0].index('K' if w else 'k'),not w);ms=list(l(s))
 if not ms:return(-B+p if chk else 0),None
 if d==0 and not chk:
  z=v(s)
  if z>=b:return z,None
  a=max(a,z);ms=[q for q in ms if r(s,q)>=0]
 best=-B;mv=None
 for q in sorted(ms,key=lambda q:r(s,q)+50*(q==KL[p]),reverse=True):
  z=-n(m(s,q),max(0,d-1+chk),-b,-a,p+1)[0]
  if z>best:best=z;mv=q
  a=max(a,z)
  if a>=b:KL[p]=q;break
 return(a if d==0 and not chk else best),mv
def c(s):
 global N
 s=f(s);ms=list(l(s))
 if not ms:return None
 z=ms[0];N=0;d=1
 while 1:
  try:_,q=n(s,d,-B,B,0);z=q or z;d+=1
  except C:break
 a,t,p=z
 return f'{chr(97+a%8)}{8-a//8}{chr(97+t%8)}{8-t//8}{p}'
def p(b,u,d):return J.load(Q.urlopen(Q.Request(b+u,J.dumps(d).encode())))
if __name__=='__main__' and(b:=O.getenv('MAKEFUN_ENV_URL')):
 b=b.rstrip('/')
 while(s:=p(b,'/game',{}))['status']!='done':
  while s['status']=='your_move':q=c(s['fen']);z=s['legal_moves'];q=q if q in z else z[0];s=p(b,'/move',{'game':s['game'],'move':q})
