import dash
from dash import dcc
from dash import html
import h5py

# HDF5 파일 불러오기
hdf = h5py.File('output.hdf5', 'r')

# 데이터셋 이름들을 리스트로 가져오기
dataset_names = list(hdf.keys())

# 그룹 설정
groups = {
    'Joint': ['joint1', 'joint2', 'joint3', 'joint4', 'joint5', 'joint6'],
    'Velocity': ['velocity1', 'velocity2', 'velocity3', 'velocity4', 'velocity5', 'velocity6']
}

# Dash 애플리케이션 생성
app = dash.Dash(__name__)

# 애플리케이션 레이아웃 설정
app.layout = html.Div([
    # Header
    html.Div([
        html.Div([
            html.Img(src='assets/logo.svg', width='180px')
        ], className='koreatech-header-logo')
    ], className='koreatech-header'),

    # 제목
    html.H1('데이터 시각화', className='title', style={'font-family': 'Arial, sans-serif'}),

    # 그룹 선택 박스
    dcc.Dropdown(
        id='group-dropdown',
        options=[{'label': group, 'value': group} for group in groups.keys()],
        value=list(groups.keys())[0]
    ),

    # 콤보박스와 그래프
    html.Div([
        # 콤보박스
        dcc.Dropdown(
            id='graph-dropdown',
            options=[{'label': name, 'value': name} for name in groups[list(groups.keys())[0]]],
            value=groups[list(groups.keys())[0]][0]
        ),

        # 그래프
        dcc.Graph(id='graph')
    ], className='graph-container')
])


# 그룹 선택 박스 콜백 함수
@app.callback(
    dash.dependencies.Output('graph-dropdown', 'options'),
    [dash.dependencies.Input('group-dropdown', 'value')]
)
def update_graph_dropdown_options(selected_group):
    return [{'label': name, 'value': name} for name in groups[selected_group]]


# 그래프 콜백 함수
@app.callback(
    dash.dependencies.Output('graph', 'figure'),
    [dash.dependencies.Input('group-dropdown', 'value'),
     dash.dependencies.Input('graph-dropdown', 'value')]
)
def update_graph(selected_group, selected_dataset):
    # 선택한 데이터셋 가져오기
    data = hdf[selected_dataset][:]

    # 그래프 생성
    figure = {
        'data': [
            {'x': list(range(len(data))), 'y': data, 'type': 'line'}
        ],
        'layout': {
            'title': selected_dataset
        }
    }

    return figure


# 애플리케이션 실행
if __name__ == '__main__':
    app.run_server(debug=True)
