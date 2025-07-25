# [Bronze I] 리그 - 5544 

[문제 링크](https://www.acmicpc.net/problem/5544) 

### 성능 요약

메모리: 33432 KB, 시간: 40 ms

### 분류

수학, 구현, 사칙연산

### 제출 일자

2025년 7월 23일 22:19:11

### 문제 설명

<p>축구 리그에 총 N개의 팀이 소속되어 있고, 1부터 N까지 번호가 매겨져 있다. 이 리그는 모든 조합의 경기가 한 번씩 열린다. 즉, N(N-1)/2 경기가 열리게 된다. 각 경기에서 많은 득점을 한 팀이 이기게 된다. 이긴 팀은 승점 3점을 가져가고, 지는 팀은 0점을 가져간다. 무승부의 경우에는 두 팀이 각각 1점씩 가져가게 된다. 리그 순위는 각 팀이 획득한 승점의 합계로 결정하고, 득실차는 생각하지 않는다. 승점의 합이 동일한 팀의 순위는 가능한 순위 중 가장 높은 것이다.</p>

<p>예를 들어, 4 팀이 리그에 참가한다고 하자. 그럼, 총 4(4-1)/2 = 6경기가 열린다. 결과는 다음과 같다고 하자. 하이픈의 왼쪽 점수는 왼쪽에 있는 팀의 점수이고, 오른쪽 점수는 위쪽에 있는 팀의 점수이다.</p>

<table class="table table-bordered" style="width:54%">
	<thead>
		<tr>
			<th style="width:6%"> </th>
			<th style="width:6%">팀 1</th>
			<th style="width:6%">팀 2</th>
			<th style="width:6%">팀 3</th>
			<th style="width:6%">팀 4</th>
			<th style="width:6%">승</th>
			<th style="width:6%">무</th>
			<th style="width:6%">패</th>
			<th style="width:6%">승점</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<th>팀 1</th>
			<td>---</td>
			<td>0 - 1</td>
			<td>2 - 1</td>
			<td>2 - 2</td>
			<td>1</td>
			<td>1</td>
			<td>1</td>
			<td>4</td>
		</tr>
		<tr>
			<th>팀 2</th>
			<td>1 - 0</td>
			<td>---</td>
			<td>1 - 1</td>
			<td>3 - 0</td>
			<td>2</td>
			<td>1</td>
			<td>0</td>
			<td>7</td>
		</tr>
		<tr>
			<th>팀 3</th>
			<td>1 - 2</td>
			<td>1 - 1</td>
			<td>---</td>
			<td>1 - 3</td>
			<td>0</td>
			<td>1</td>
			<td>2</td>
			<td>1</td>
		</tr>
		<tr>
			<th>팀 4</th>
			<td>2 - 2</td>
			<td>0 - 3</td>
			<td>3 - 1</td>
			<td>---</td>
			<td>1</td>
			<td>1</td>
			<td>1</td>
			<td>4</td>
		</tr>
	</tbody>
</table>

<p>승점이 가장 높은 팀 2가 1위가 된다. 그 다음으로 승점이 높은 팀은 팀 1과 팀 4이며, 두 팀의 순위는 2위이다. 마지막으로 승점이 가장 낮은 팀 3은 4위가 된다.</p>

<p>모든 경기의 결과가 주어졌을 때, 각 팀의 순위를 구하는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫째 줄에 팀의 수 N (2 ≤ N ≤ 100)가 주어진다. 다음 N(N-1)/2개 줄에는 각 경기의 결과가 주어진다. 경기의 결과는 A B C D와 같이 네 개의 정수로 나타내며, A팀이 C점, B팀이 D점을 획득했음을 의미한다. A와 B는 항상 다르다. 한 경기의 결과가 여러 번 주어지는 경우는 없다.</p>

### 출력 

 <p>출력은 총 N줄을 출력한다. i번째 줄에는 팀 i의 순위를 출력한다.</p>

