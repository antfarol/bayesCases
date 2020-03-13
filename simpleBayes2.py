theta=np.linspace(0.1, 0.9, 5) # set of different possible thetas

f,ax = plt.subplots(len(theta), 1,
                    sharex=True, sharey=True,
                    figsize=(8, 7), constrained_layout=True)

for j in range(len(theta)):        
    p = theta[j]        
    y = stats.binom(n=N, p=p).pmf(x)        
    ax[j].vlines(x, 0, y, colors='C0', lw=5)        
    ax[j].set_ylim(0, 0.5)
    ax[j].plot(0, 0, label="N = {:3.1f}\nθ ={:3.2f}".format(N,p))
    ax[j].axvline(x=success, color='C4', linestyle='--')
        
    ax[j].legend()
    ax[4].set_xlabel('number of success')        
    ax[0].set_xticks(x)
