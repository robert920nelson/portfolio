getwd()
setwd("C:/Users/rob/Documents/R scripts")
nba <- read.csv("nba_logreg_clean.csv")
str(nba)
table(nba$TARGET_5Yrs)
prop.table(table(nba$TARGET_5Yrs))

train_sample <- sample(1:nrow(nba),size = 500)
nba_train <- nba[train_sample,]
nba_test <- nba[-train_sample,]

install.packages("randomForest")
library(randomForest)
set.seed(100)
nba_rf <- randomForest(TARGET_5Yrs ~ ., data = nba_train)
nba_rf_pred <- predict(nba_rf, nba_test)
confusionMatrix(nba_rf_pred, nba_test$TARGET_5Yrs)