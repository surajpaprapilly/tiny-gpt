import torch
import torch.nn as nn

# seq_len = How long each sequence is (128 in our case)
# embed_dim = How many dimensions EACH token should be
# num_heads = number of attention heads (1 in this case)
# head_dim = Number of dimension of each attention head (Q,K,V) (128 in this case)

class SingleHeadAttention(nn.Module):
    def __init__(self, embed_dim, head_dim):
        super().__init__()
        self.q_proj = nn.Linear(embed_dim,head_dim)
        self.k_proj = nn.Linear(embed_dim,head_dim)
        self.v_proj = nn.Linear(embed_dim,head_dim)
        self.head_dim = head_dim
        self.embed_dim = embed_dim


    def forward(self,x):
        q = self.q_proj(x)
        k = self.k_proj(x)
        v = self.v_proj(x)

        # Calculate the attention score. How much a token at i attends to a token at j
        scores = (q @ k.transpose(-2, -1))/(self.head_dim ** 0.5)

        # Apply causal mask
        seq_len = q.shape[0]
        scores = scores.masked_fill(~torch.tril(torch.ones(seq_len,seq_len)).bool(),float('-inf'))
        
        # Apply softmax
        weights = torch.softmax(scores, dim=-1)

        out = weights @ v

        return out

        




