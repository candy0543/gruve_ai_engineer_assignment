import argparse
import pandas as pd
import joblib

def load_model(model_path):
    return joblib.load(model_path)

def predict(model, data):
    return model.predict(data)

def main(args):
    # Load unseen data
    df = pd.read_csv(args.input)

    model = load_model(args.model_path)

    # Predict
    preds = predict(model, df)

    # Save output
    output = pd.DataFrame({"readmitted": preds})
    output.to_csv(args.output, index=False)

    print(f"Predictions saved to {args.output}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=str, required=True)
    parser.add_argument("--model_path", type=str, default="processed/autogluon_model/models/LightGBMXT_BAG_L1/model.pkl")
    parser.add_argument("--output", type=str, default="outputs/predictions.csv")

    args = parser.parse_args()
    main(args)