
'''
implement ROC curve (Receiver Operating Characteristic curve)

'''

import matplotlib.pyplot as plt

class ROC(object):

    def confusion_matrix(self,y_test,y_pred_probability,threshold,output_label):
        # true positive(tp), true negative(tn), false positive(fp), false negative(fn)
        tp,tn,fp,fn=0,0,0,0
        bool_output=[]
        for element in y_test:
            if element==output_label:
                bool_output.append(1)
            else:
                bool_output.append(0)
        for truth, probability in zip(bool_output, y_pred_probability):
            if probability > threshold:                      
                if truth:
                    tp += 1
                else:           
                    fp += 1
            else:
                if not truth:
                    tn += 1                          
                else:
                    fn += 1
        return tp,tn,fp,fn
    
    # calculate False Positive Rate (FPR) and True Positive Rate (TPR)
    def fpr_and_tpr(self,y_test,y_pred_probability,threshold,output_label):
        tp,tn,fp,fn=self.confusion_matrix(y_test,y_pred_probability,threshold,output_label)
        fpr=fp/(fp+tn)      # False Positive Rate (fpr)
        tpr=tp/(tp+fn)      # True Positive Rate (tpr)
        return fpr,tpr

    def plot(self,y_test,y_pred_probability,output_label):
        x=[]
        y=[]
        threshold=0
        # set threshold
        for i in range(0,11,1):
            fpr,tpr=self.fpr_and_tpr(y_test,y_pred_probability,threshold,output_label)
            x.append(fpr)
            y.append(tpr)
            threshold+=0.1
        plt.xlabel('FPR')
        plt.ylabel('TPR')
        plt.plot([0,1],[0,1],'--')
        plt.plot(x,y,'r')
        plt.show()