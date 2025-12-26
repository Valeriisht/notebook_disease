# For each model
MODEL_CONFIGS = {
    "CatBoost": {
        "params": {
            "iterations": 1000,
            "learning_rate": 0.2,
            "early_stopping_rounds": 10,
            "eval_metric": "MultiClass",
            "verbose": 0,
            "random_state": 42,
        },
        "needs_cat_features": False,
        "use_onehot": True,
        "use_eval_set": True,
        "needs_imputation": False,
        "shap" : True,
    },
    "XGBoost": {
        "params": {
            "n_estimators": 1000,
            "learning_rate": 0.2,
            "early_stopping_rounds": 20,
            "eval_metric": "mlogloss",
            "random_state": 42,
            "enable_categorical": True,
            "verbose": False, 
            "objective":'multi:softprob',
            "nthread": 8,  
            "tree_method": "hist",
            "device": "cuda"

        },
        "needs_cat_features": False,
        "use_onehot": True,
        "use_eval_set": True,
        "needs_imputation": False,
        "shap" : False, 
    },

    "LightGBM": {
        "params": {
            "n_estimators": 1000,
            "learning_rate": 0.2,
            "early_stopping_round": 10,
            "random_state": 42,
            "verbose": -1
        },
        "needs_cat_features": False,
        "use_onehot": True,
        "use_eval_set": True,
        "needs_imputation": False, 
        "shap" : True   
    },
    "SVM": {
        "params": {
            "probability": True,
            "random_state": 42
        },
        "needs_cat_features": False,
        "use_onehot": True,
        "use_eval_set": False,
        "needs_imputation": True,
        "shap" : False   
    },
    "RandomForest": {
        "params": {
            "random_state": 42
        },
        "needs_cat_features": False,
        "use_onehot": True,
        "use_eval_set": False,
        "needs_imputation": True, 
        "shap" : False     
    },
    "LogisticRegression": {
        "params": {
            "random_state": 42
        },
        "needs_cat_features": False,
        "use_onehot": True,
        "use_eval_set": False,
        "needs_imputation": True, 
        "shap" : False     
    }
}
