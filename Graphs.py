from __future__ import print_function
import sys
		
time = 0		
def BFS(G, color, d, p, e, s):
	for u in G.keys():
		color.update({u:"WHITE"})
		d.update({u: -1})
		p.update({u: None})

	color.update({s: "GRAY"})
	d.update({s: 0})
	p.update({s: None})		
		
	Q = []
	Q.append(s)
	while len(Q) is not 0:
		print(Q)
		u = Q.pop(0)
		for v in G.get(u):
			if color.get(v) == "WHITE":
				e.update({u+v:"Tree"})
				color.update({v: "GRAY"})
				d.update({v: d.get(u) + 1})
				p.update({v: u})
				Q.append(v)
			elif color.get(v) == "GRAY":
				e.update({u+v:"Back"})
			else:
				e.update({u+v:"Cross"})
				
		color.update({u:"BLACK"})
		

def DFS(G, color, d, p, f, e, s):
	for u in G.keys():
		color.update({u:"WHITE"})
		p.update({u:None})
	global time
	time = 0
	
	DFSVisit(G, color, d, p, f, e, s)
	for u in G.keys():
		if color.get(u) == "WHITE":
			DFSVisit(G, color, d, p, f, e, u)
			
			
def DFSVisit(G, color, d, p, f,e, u):
	global time
	time += 1
	d.update({u:time})
	color.update({u:"GRAY"})
	for v in G.get(u):
		if color.get(v) == "WHITE":
			e.update({u+v:"Tree"})
			p.update({v:u})
			DFSVisit(G, color, d, p, f, e, v)
		elif color.get(v) == "GRAY":
			e.update({u+v:"Back"})
		else:
			if d.get(u) < d.get(v):
				e.update({u+v:"Forward"})
			else:
				e.update({u+v:"Cross"})
	color.update({u:"BLACK"})
	time += 1
	f.update({u:time})


def printPath(G, color, d, p, s, v):
	if v==s:
		print(s)
	elif p.get(v) is None:
		print("No Path from %s to %s exists" %(s,v))
	else:
		printPath(G, color, d, p, s, p.get(v))
		print(v)
		
		
def main():
	num = int(sys.stdin.readline())
	G = {}
	color = {}
	d = {}
	p = {}
	f = {}
	e={}
	for i in range(num):
		line = sys.stdin.readline().split()
		a = line[0]
		line.pop(0)
		G.update({a:line})
	
	BFS(G, color, d, p, e, 's')
# 	printPath(G, color, d, p, 's', 'y')
	
# 	DFS(G, color, d, p, f,e, 'u')
# 	print(d)
	print(e)
# 	printPath(G, color, d, p, 'u', 'u')
	
if __name__ == "__main__":main()