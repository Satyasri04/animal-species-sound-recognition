import matplotlib.pyplot as plt
import seaborn as sns
import io
import base64

def plot_prediction_history(history_dict):
    plt.figure(figsize=(6,4))
    sns.barplot(x=list(history_dict.keys()), y=list(history_dict.values()))
    plt.ylabel("Count")
    plt.title("Predicted Species Distribution")
    
    # Convert to base64 for HTML embedding
    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    img_base64 = base64.b64encode(buf.read()).decode('utf-8')
    buf.close()
    return img_base64
