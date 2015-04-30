class wocc():
    def __init__(self, get_features):
        self.data = {}
        self.feat = get_features
    
    def train(self, X_data, Y_data):
        Xs = [self.feat(x) for x in X_data]
        for i in range(len(Y_data)):
            cls = Y_data[i]
            for w in Xs[i]:
                if cls in self.data.keys():
                    self.data[cls].setdefault(w,0)
                    self.data[cls][w] += 1
                else:
                    self.data.setdefault(cls,{w:1})
    
    def classify(self, X_data):
        Xs = [self.feat(x) for x in X_data]
        Y_data = []
        clss = self.data.keys()
        for x in Xs:
            cls_occs = [0 for c in clss]
            for j in range(len(clss)):
                cls = clss[j]
                n = sum([self.data[cls][w] for w in x if w in self.data[cls].keys()])
                cls_occs = n
            p = cls_occs.index(max(cls_occs))
            Y_data.append(clss[p])
        return Y_data
