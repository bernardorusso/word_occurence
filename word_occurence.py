class wocc():
    def __init__(self, get_features):
        self.data = {}
        self.feat = get_features
    
    def train(self, X_data, Y_data):
        Xs = [self.feat(x) for x in X_data]
        for i in range(len(Y_data)):
            cls = Y_data[i]
            if cls in self.data.keys():
                self.data[cls] += Xs[i]
            else:
                self.data[cls] = Xs[i]
    
    def classify(self, X_data):
        Xs = [self.feat(x) for x in X_data]
        for i in self.data.keys():
            self.data[i] = unique_elts(self.data[i])
        Y_clss = []
        for x in Xs:
            clss_prob = dict([[cls,0] for cls in self.data.keys()])
            for cls in self.data.keys():
                cls_fts = self.data[cls]
                clss_prob[cls] += len([feat for feat in x if feat in cls_fts])
            cls = max(clss_prob.iteritems(), key=op.itemgetter(1))[0]
            Y_clss.append(cls)
        return Y_clss
