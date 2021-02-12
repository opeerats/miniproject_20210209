from flask import Flask, render_template, request
import requests
import random

app = Flask(__name__)

@app.route('/')
def home():
    # HTML 반환해주기
    # 반드시 templates 폴더 안에 위치해야합니다.
    # render_template 불러와주기
    return render_template('home.html')


@app.route('/service_intro')
def service_intro():
    # HTML 반환해주기
    # 반드시 templates 폴더 안에 위치해야합니다.
    # render_template 불러와주기
    return render_template('service_intro.html')

# render_template 사용해보기
# == 사용자에게 보여줄 데이터를 HTML에 담기
@app.route('/service')
def service():
    # HTML 반환해주기
    # 반드시 templates 폴더 안에 위치해야합니다.
    # render_template 불러와주기


    random_list = ['BBQ 황금 올리브 치킨', 'BHC 뿌링클', '교촌치킨 레드콤보', '굽네치킨 고추바사삭', 'BHC 맛초킹']
    random_choice = random.choice(random_list)
    # 랜덤한 메뉴를 선정한다.
   
    선택 = request.args.get('선택', default = 'ns-abc-aaa', type = str)
    if 선택 == '아무거나':
        random_menu = random_choice
    else:
        random_menu = '뭐 먹을래?'

    
    return render_template('service.html', random_menu=random_menu)



# @app.route('/test')
# def test():
#     ns = request.args.get('선택', default = 'ns-abc-aaa', type = str)
#     if ns == '아무거나':
#         sample = 'random_menu'
#     else:
#         sample = 'sample_defalt'
#     return render_template('test.html', ns=ns, sample=sample)













# 파일 수정 시, 자동으로 반영해주는 코드
# 서버 껐다킬 필요 없음.
# 이제부터 python app.py로 서버 실행!
if __name__ == '__main__':
    app.run(debug=True)