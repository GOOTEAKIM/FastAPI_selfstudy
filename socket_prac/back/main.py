# from fastapi import FastAPI, WebSocket, WebSocketDisconnect

# app = FastAPI()

# @app.websocket("/ws/agv")
# async def websocket_endpoint(websocket: WebSocket):
#     await websocket.accept()  # WebSocket 연결 수락
#     try:
#         while True:
#             # 클라이언트로부터 메시지 받기
#             data = await websocket.receive_text()
#             print(f"Received from client: {data}")
            
#             # 받은 데이터를 클라이언트에게 다시 전송
#             await websocket.send_text(f"AGV 위치 정보: {data}")
#     except WebSocketDisconnect:
#         print("WebSocket 연결 해제됨")
        
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from typing import List

app = FastAPI()

# 현재 연결된 클라이언트 목록
active_connections: List[WebSocket] = []

@app.websocket("/ws/agv")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()  # WebSocket 연결 수락
    active_connections.append(websocket)  # 클라이언트를 목록에 추가

    try:
        while True:
            # 클라이언트로부터 메시지 받기
            data = await websocket.receive_text()
            print(f"Received from client: {data}")

            # 받은 데이터를 모든 클라이언트에게 전송
            for connection in active_connections:
                await connection.send_text(f"AGV 위치 정보: {data}")

    except WebSocketDisconnect:
        print("WebSocket 연결 해제됨")
        active_connections.remove(websocket)  # 연결 해제 시 클라이언트 목록에서 제거
