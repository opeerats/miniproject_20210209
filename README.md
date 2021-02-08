

---



<span style="color: #0070c2; font-size: 25px; font-weight: bold">| mini project 2021_02_09</span> 



본 미니프로젝트는 2021년 2월 2째주 주말 진행하는 미니프로젝트입니다.



```
git clone https://github.com/opeerats/miniproject_20210209.git
```

로 일단 clone을 받아주세요. 

자동으로 remote repository가 등록됩니다.



~~~python
git branch brchA 

git branch brchB

 git branch brchC
~~~

와 같이 branch를 파서 진행할 예정입니다.



각자 자신의 작업이 끝났다면, 

~~~python
git add .
git commit -m "기능 구현 완료"

git checkout master
git merge brchB
git push origin master
~~~

와 같이 진행하여 자신의 작업상황을 github에 push 할 수 있습니다.



~~~python
git checkout master

git pull origin master
~~~

다른 사람들은 위와 같이 입력하여 업로드된 사항을 pull하여 업데이트 할 수 있습니다.

반드시 pull을 받기 전에, 본인이 작업중이던 사항을 commit해두고 pull해주세요



~~~python
git checkout brchA

git merge master
~~~

이제 위와 같이 입력하여 자신의 작업본에 반영할 수 있습니다.





이는 github를 이용하여 협업할 때 주로 쓰이는 branch기능을 이용한 것이지만,

저도 잘 모르기 때문에...

굳이 안써도 됩니다.

---

- 참고

[victoree님의 블로그](https://victorydntmd.tistory.com/91)