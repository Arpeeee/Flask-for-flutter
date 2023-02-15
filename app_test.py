# 載入必須套件
from flask import Flask, request, redirect
from flask_restful import Resource, Api

# from flask_cors import CORS


# 創建Flask app物件
app = Flask(__name__)
# CORS(app)
api = Api(app)

# 創建一個陣列(創一個名為apple物品當測試)，存放品項
items = [{"name": "apple", "price": 32.3}]
url = {"URL": "https://bot.mds.com.tw/rescue/gotoweb119/"}
url2 = {"URL": "https://www.flutterbeads.com/if-else-statement-in-flutter-widget/"}


# @app.route("/")
class URL(Resource):
    # 單一品項查詢
    def get(self):
        # item = next(filter(lambda x: x['name'] == name, items), None)
        return url, 200

    # 建制新品項
    def post(self):
        data = request.get_json()
        print(data)
        if data["name"] == "123456":
            return url, 201
        else:
            return url2, 201


api.add_resource(URL, "/URLtest")
# api.add_resource(ItemsList, "/items")

if __name__ == "__main__":
    app.run(port=5400, debug=True)
