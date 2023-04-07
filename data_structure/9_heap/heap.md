# 9. 우선순위 큐

### 📝우선순위 큐란?
- 데이터들이 우선순위를 가지고 있고 우선순위가 높은 데이터가 먼저 나가게 된다.
-우선순위 큐는 배열, 연결리스트, 히프로 구현이 가능하고 가장 효율적인 구조는 히프이다.

<table>
  <tr>
  	<th width="150">표현방법</th>
  	<th width="150">삽입</th>
 	<th width="150">삭제</th>
 </tr>
  <tr>
    <td>순서없는 배열</td>
    <td>O(1)</td>
    <td>O(n)</td>
  </tr>
  <tr>
    <td>순서없는 연결리스트</td>
    <td>O(1)</td>
    <td>O(n)</td>
  </tr>
  <tr>
    <td>정렬된 배열</td>
    <td>O(n)</td>
    <td>O(1)</td>
    
  </tr>
  <tr>
    <td>정렬된 연결리스트</td>
    <td>O(n)</td>
    <td>O(1)</td>
    
  </tr>
  <tr>
    <td>히프</td>
    <td>O(logn)</td>
    <td>O(logn)</td>
  </tr>
</table>

### 📝히프트리란
- 완전이진트리
- 가장 큰 값은 루트노드
- 중복된 값 허용

### 📝삽입연산
```
✏️c언어로 코드 작성

//----히프정의
#define MAX 200 //배열크기
typedef struct{
	int key; //배열 요소들
}element;

typedef struct{
	element heap[MAX]; //히프트리 배열 생성
    	int heap_size;//현재 히프크기를 알기위함
        	      //삽입하면 증가 삭제하면 감소
}Heaptype;

//삽입연산
void insert_max_heap(HeapType* h, element item){
	int i;
        i=++(h->heap_size); 
    //히프크기를 증가(요소 삽입할 공간 마련
    
    //트리를 거슬러 올라가면서 부모노드와 비교하는 과정
    //while문을 통해 삽입위치가 정해진다
    while((i!=1)&&(item.key>h->heap[i/2].key)){
    	//부모노드가 작으므로 i번째에 부모노드 삽입
        h->heap[i]=h->heap[i/2];
        //부모인덱스로 이동
    	i/=2;
    }
}
h->heap[i]=item; //새로운 노드를 삽입
```
#### 🔦코드분석
![](https://images.velog.io/images/mseo39/post/7bbe81e0-7a24-4411-909a-d517ccae043c/1.png)
![](https://images.velog.io/images/mseo39/post/7d02729c-0972-4147-8edb-cb61b4956184/2.png)