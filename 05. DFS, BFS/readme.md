탐색(Search)이란 많은 양의 데이터 중에서 원하는 데이터를 찾는 과정을 의미한다.
프로그래밍에서는 그래프, 트리 등의 자료구조 안에서 탐색을 하는 문제를 자주 다룬다.
대표적인 탐색 알고리즘으로 DFS와 BFS를 꼽을 수 있는데, 이 두 알고리즘의 원리를 제대로 이해해야 코딩 테스트의 탐색 문제 유형을 풀 수 있다.
자료구조(Data Structure)란 '데이터를 표현하고 관리하고 처리하기 위한 구조'를 의미한다. 그중 스택과 큐는 자료구조의 기초 개념으로 삽입(Push)와 삭제(Pop) 두 핵심적인 함수로 구성된다.

- 스택(Stack)은 박스 쌓기에 비유할 수 있다. 이러한 구조를 선입후출(First In Last Out) 구조 또는 후입선출(Last In First Out) 구조라고 한다.

- 큐(Queue)는 대기 줄에 비유할 수 있다. 이러한 구조를 선입선출(First In First Out) 구조라고 한다.

- 재귀 함수(Recursive Function)란 자기 자신을 다시 호출하는 함수를 의미한다.

스택과 큐, 재귀 함수는 DFS와 BFS에서 가장 중요한 개념이라 DFS/BFS를 배우기에 앞서 간단하게 설명했다. 이제부터 DFS/BFS 알고리즘을 살펴보자.

- DFS(Depth-First Search), 깊이 우선 탐색이라고도 부르며, 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘이다. DFS는 스택 자료구조(혹은 재귀 함수)를 이용하며, 구체적인 동작 과정은 다음과 같다.
  1. 탐색 시작 노드를 스택에 삽입하고 방문 처리한다.
  2. 스택의 최상단 노드에 방문하지 않은 인접한 노드가 하나라도 있으면 그 노드를 스택에 넣고 방문 처리한다. 방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼낸다.
  3. 더 이상 2번의 과정을 수행할 수 없을 때까지 반복한다.

- BFS(Breadth-First Search), 너비 우선 탐색이라고도 부르며, 그래프에서 가까운 노드부터 우선적으로 탐색하는 알고리즘이다. BFS는 큐 자료구조를 이용하며, 구체적인 동작 과정은 다음과 같다.
  1. 탐색 시작 노드를 큐에 삽입하고 방문 처리를 한다.
  2. 큐에서 노드를 꺼낸 뒤에 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리한다.
  3. 더 이상 2번의 과정을 수행할 수 없을 때까지 반복한다.