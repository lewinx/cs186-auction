###############################################################################
# STAT186 Final Project
###############################################################################

library(ggplot2)

election <- read.csv("~/Dropbox/CS186/cs186-auction/final_project/data_normalprefs.csv")
election <- read.csv("~/Dropbox/CS186/cs186-auction/final_project/data_normalprefs_noisy.csv")
election <- read.csv("~/Dropbox/CS186/cs186-auction/final_project/data_uniformprefs.csv")
election <- read.csv("~/Dropbox/CS186/cs186-auction/final_project/data_uniformprefs_noisy.csv")

my.names <- c('election', 'mean_loss')

df <- as.data.frame(t(data.frame(Plurality = mean(election$plurality_loss),
                 Majority = mean(election$majority_loss),
                 Borda = mean(election$Borda_loss),
                 Democracy21 = mean(election$democracy21_loss))))

df$election <- rownames(df)
df$mean_loss <- df$V1
df$V1 <- NULL
rownames(df) <- NULL

ggtitle <- "Mean Loss of Voting Mechanisms (True Normally-distributed Preferences)"
ggtitle <- "Mean Loss of Voting Mechanisms (Noisy Normally-distributed Preferences)"
ggtitle <- "Mean Loss of Voting Mechanisms (True Uniformly-distributed Preferences)"
ggtitle <- "Mean Loss of Voting Mechanisms (Noisy Uniformly-distributed Preferences)"

png("4.png", width=10, height=8, units="in", res=150)
ggplot(df, aes(x = factor(election), y = mean_loss)) + 
  geom_bar(aes(fill = factor(election)),stat = "identity") +
  geom_text(aes(y=mean_loss, ymax=mean_loss, label=round(mean_loss,2)), 
            position= position_dodge(width=0.9), vjust=-.25, color="black") +
  xlab("Voting Mechanism") + ylab("Mean Utility Loss") + 
  ggtitle(ggtitle) + 
  guides(fill=guide_legend(title='Election Types'))
dev.off()


