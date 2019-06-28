import seaborn as sns
import matplotlib.pyplot as plt

sns.set()
tips = sns.load_dataset("tips")
sns.relplot(x= "total_bill", y = "tip", col = "time", hue = "smoker", style = "smoker", 
            size = "size", data = tips)

dots = sns.load_dataset("dots")

sns.relplot(x = "time", y = "firing_rate", col = "align", hue = "choice", 
            style = "choice", size = "coherence", facet_kws = dict(sharex = False), kind = "line",
            legend ="full", data = dots)

fmri = sns.load_dataset("fmri")

sns.relplot(data=fmri, x="timepoint", y="signal",col="region",hue="event",style="event",kind="line")

sns.lmplot(x="total_bill",y="tip",col="time",hue="smoker", data=tips)

sns.catplot(x="day", y="total_bill", hue="smoker",
            kind="swarm", data=tips);
plt.show()
