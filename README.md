# 👩🏻‍💻 Jisu's Portfolio

## 기술 스택
- React
- Django Rest Framework
- MySQL


##  기능 / 소개
- Mobile, Tablet, Desktop에 맞추어 반응형으로 제작했습니다.
- Home, About, Project, Contact 섹션으로 나누어져 있습니다.
- 프로젝트 정보(Project Detail)는 MySQL과 DRF를 이용하여 동적으로 정보를 나타냈습니다.
- 장고의 Admin 페이지를 통해 프로젝트의 정보를 입력하여 DB에 저장하였습니다.

## Repositories
- Design:https://www.figma.com/file/nwiF7fveKHZ2hFJIpKxtkd/Portfolio?node-id=0%3A1
- Client:https://github.com/Jsgithubchannel/portfolio-front
- Server:https://github.com/Jsgithubchannel/portfolio-back

## Settings

### Backend
```
git clone https://github.com/Jsgithubchannel/portfolio-back.git
cd portfolio-back
pip install -r requirements.txt
cd portfolio
python manage.py runserver

Please, put attached secrets.json, my_settings.py into the portfolio directory.
```
### Frontend
```
git clone https://github.com/Jsgithubchannel/portfolio-front.git
cd portfolio-front
npm install
npm start

Please, put attached the .env file into the portfolio-front directory.
```


## Preview

### Home
- 간단한 소개와 Github, Blog, LinkedIn 링크, 정보를 나타냈습니다.

- #### Mobile
![image](https://user-images.githubusercontent.com/66022264/174485942-7c730031-81b6-4f70-957d-ef27fa844160.png)
- #### Tablet
![image](https://user-images.githubusercontent.com/66022264/174485945-bcc53478-d7bd-4517-ae5c-b4ff33bf831a.png)
- #### PC
![image](https://user-images.githubusercontent.com/66022264/174485956-b6d5cd89-3dce-4c66-a52a-5c722dd9fad4.png)


### About
- 기술 스택을 나열했습니다.
- Desktop 버전에서 커서 hover를 하면, 아이콘이 움직이는 효과를 넣었습니다.
![image](https://user-images.githubusercontent.com/66022264/174486333-2908c86d-e2e7-4edc-9509-84c1e8fd82f0.png)


### Project
- 대표 프로젝트 4개의 이미지를 나열하였습니다. 
- 이미지 hover시, 해당 프로젝트명이 나타납니다.
![image](https://user-images.githubusercontent.com/66022264/174486445-e9116379-0e38-40af-8394-1768c48f53e5.png)


### Project Detail
- 클릭한 프로젝트에 관한 정보(프로젝트명, 기간, 소개 등)가 나타납니다.
![image](https://user-images.githubusercontent.com/66022264/174486627-6e4f823f-0fd4-47d8-90d4-81903c19af3a.png)
