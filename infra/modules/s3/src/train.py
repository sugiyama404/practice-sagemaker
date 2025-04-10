import argparse
import os
import pandas as pd
import numpy as np
import xgboost as xgb
from sklearn.model_selection import train_test_split

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    # ハイパーパラメータ
    parser.add_argument('--max_depth', type=int, default=3)
    parser.add_argument('--eta', type=float, default=0.1)
    parser.add_argument('--objective', type=str, default='binary:logistic')
    parser.add_argument('--num_round', type=int, default=10)

    # SageMakerの環境変数
    parser.add_argument('--model_dir', type=str, default=os.environ.get('SM_MODEL_DIR', './model'))
    parser.add_argument('--train', type=str, default=os.environ.get('SM_CHANNEL_TRAIN', './data'))
    parser.add_argument('--validation', type=str, default=os.environ.get('SM_CHANNEL_VALIDATION', None))

    args, _ = parser.parse_known_args()

    # データの読み込み
    data_path = os.path.join(args.train, 'sample_data.csv')
    data = pd.read_csv(data_path)

    # 特徴量とターゲットの分離
    X = data.drop('class', axis=1)
    y = data['class']

    # トレーニングデータとバリデーションデータに分割
    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

    # DMatrixに変換
    dtrain = xgb.DMatrix(X_train, label=y_train)
    dval = xgb.DMatrix(X_val, label=y_val)

    # パラメータの設定
    params = {
        'max_depth': args.max_depth,
        'eta': args.eta,
        'objective': args.objective
    }

    # トレーニング
    watchlist = [(dtrain, 'train'), (dval, 'validation')]
    model = xgb.train(params, dtrain, args.num_round, evals=watchlist)

    # モデルの保存
    os.makedirs(args.model_dir, exist_ok=True)
    model_path = os.path.join(args.model_dir, 'xgboost-model')
    model.save_model(model_path)
