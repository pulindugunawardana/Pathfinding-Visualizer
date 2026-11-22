import pygame

pygame.init()
screen = pygame.display.set_mode((600, 600))
LAYER1 = pygame.Surface((600, 600),pygame.SRCALPHA)
LAYER2 = pygame.Surface((600, 600),pygame.SRCALPHA)
LAYER3 = pygame.Surface((600, 600),pygame.SRCALPHA)
clock = pygame.time.Clock()

pygame.display.set_caption('Pathfinding Visualizer')

step_delay = 500
elapsed = 0
current_step = 0

visited = set()

running = True

green = (85, 89, 52,255)
black = (0, 0, 0,255)
red = (140, 91, 62,255)
grey = (100,100,100,255)
white = (255,255,255,255)
mouse_pos = (0,0)

def bfs(adj):
    V = len(adj)
    visited = [False]*V
    res = []

    src = 0
    q = []
    visited[src] = True
    q.append(src)

    while q:
        q.reverse()
        curr = q.pop()
        res.append(curr)

        for x in adj[curr]:
            if not visited[x]:
                visited[x]=True
                q.append(x)                     
    return res

def dfsRec(adj, visited, s, res):
    visited[s] = True
    res.append(s)

    for i in adj[s]:
        if not visited[i]:
            dfsRec(adj, visited, i, res)


def dfs(adj):
    visited = [False] * len(adj)
    res = []
    dfsRec(adj, visited, 0, res)
    return res

nodes = [
    (300, 90, 0),
    (150, 210, 1),
    (450, 210, 2),
    (150, 390, 3),
    (450, 390, 4),
    (300, 510, 5)
]

def addEdge(adj, u, v):
    adj[u].append(v)
    adj[v].append(u)


def drawGraph():
    V = len(nodes)
    adj = []
    
    for i in range(V):
        adj.append([])
        
    addEdge(adj, 1, 2)
    addEdge(adj, 1, 0)
    addEdge(adj, 2, 0)
    addEdge(adj, 2, 3)
    addEdge(adj, 2, 4)
    addEdge(adj, 1, 5)
    addEdge(adj, 1, 4)
    addEdge(adj, 3, 5)

    return adj,V

adj,V = drawGraph()
res1 = bfs(adj)
res2 = dfs(adj)

res = [res1,res2]
current_al = None

Button1 = pygame.Rect(420, 30, 60, 30)
Button2 = pygame.Rect(510, 30, 60, 30)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if Button1.collidepoint(event.pos):
                    current_al = 0
                    current_step = 0
                    elapsed = 0
                    visited.clear()
                if Button2.collidepoint(event.pos):
                    current_al = 1
                    current_step = 0
                    elapsed = 0
                    visited.clear()

    dt = clock.tick(60)
    elapsed += dt

    if current_al is not None:
        if elapsed >= step_delay and current_step < len(res[current_al]):
            visited.add(res[current_al][current_step])
            current_step += 1
            elapsed = 0

    screen.fill((242, 230, 216))
    LAYER1.fill((242, 230, 216,0))
    LAYER2.fill((242, 230, 216,0))

    for u in range(V):
        for v in adj[u]:
            if nodes[u][2] in visited :
                pygame.draw.line(LAYER2, green, nodes[u][:2], nodes[v][:2], width=4)
            else:
                pygame.draw.line(LAYER2, red, nodes[u][:2], nodes[v][:2], width=4)



    pygame.draw.rect(LAYER2,grey,Button1)
    pygame.draw.rect(LAYER2,grey,Button2)

    if current_al == 0:
        pygame.draw.rect(LAYER2,(89, 62, 46), Button1)
    else:
        pygame.draw.rect(LAYER2, (140, 91, 62), Button1)

    if current_al == 1:
        pygame.draw.rect(LAYER2, (89, 62, 46), Button2)
    else:
        pygame.draw.rect(LAYER2, (140, 91, 62), Button2)
        
    screen.blit(LAYER2,(0,0))

    for x,y,z in nodes:
        if z in visited:
            node_colour = green
        else:
            node_colour = red
        pygame.draw.circle(LAYER1,node_colour, (x, y), 50)

    font = pygame.font.Font('freesansbold.ttf', 45)
    font2 = pygame.font.Font('freesansbold.ttf', 25)

    labels = ["A", "B", "C", "D", "E", "F"]
    
    screen.blit(LAYER1,(0,0))
    
    for label,position in zip(labels,nodes):
        text = font.render(label,True, white)
        textRect = text.get_rect()
        textRect.center = position[:2]
        screen.blit(text,textRect)

    Butt1 = font2.render("BFS",True, white)
    buttrect = Butt1.get_rect()
    buttrect.center = (450,45)
    screen.blit(Butt1,buttrect)

    Butt2 = font2.render("DFS",True, white)
    buttrect1 = Butt2.get_rect()
    buttrect1.center = (540,45)
    screen.blit(Butt2,buttrect1)

    pygame.display.flip()

pygame.quit()
