mrp <- function(meanup,meanrep,timelim,m,r,dbg=FALSE) {
   simlist <- newsim(timelim,m+r,  # new
      appcols=c('startqtime','startuptime'),dbg=dbg)
   simlist$reactevent <- mrpreact  
   simlist$uprate <- 1.0 / meanup
   simlist$reprate <- 1.0 / meanrep
   simlist$nmach <- m
   simlist$nrepairpersons <- r
   simlist$queue <- newqueue(simlist)  
   simlist$nup <- m  
   simlist$nrepbusy <- 0  
   simlist$breakevnt <- 1  
   simlist$repairevnt <- 2  
   simlist$nrepairs <- 0
   simlist$totqtime <- 0.0
   simlist$totuptime <- 0.0

   # START NEW CODE
   simlist$coffevnt <- 3
   # END NEW CODE

   for (i in 1:m) {
      whenbreak <- rexp(1,simlist$uprate)
      schedevnt(simlist,whenbreak,simlist$breakevnt,appdata=c(NA,0))
   }

   mainloop(simlist)

   cat("mean queuing time:  ")
   print(simlist$totqtime / simlist$nrepairs)
   cat("proportion up per machine:  ")
   print(simlist$totuptime / (simlist$nmach * simlist$timelim))
}

mrpreact <- function(evnt,simlist) {
   etype <- evnt['evnttype']
   if (etype == simlist$breakevnt) {  
      simlist$totuptime <- 
         simlist$totuptime + simlist$currtime - evnt[4]
      nrepb <- simlist$nrepbusy
      if (nrepb < simlist$nrepairpersons) {  
         simlist$nrepbusy <- nrepb + 1
         repduration <- rexp(1,simlist$reprate)
         schedevnt(simlist,simlist$currtime+repduration,simlist$repairevnt,
            appdata=c(NA,NA))
      } else {  
         evnt[3] <- simlist$currtime
         appendfcfs(simlist$queue,evnt)
      }
   } else if (etype == simlist$repairevnt) {  
      simlist$nrepairs <- simlist$nrepairs + 1
      uptime <- rexp(1,simlist$uprate)
      schedevnt(simlist,simlist$currtime+uptime,simlist$breakevnt,
         appdata=c(NA,simlist$currtime))
      simlist$nrepbusy <- simlist$nrepbusy - 1
      if (nrow(simlist$queue$m) > 0) {  
         qhead <- delfcfs(simlist$queue)
         simlist$totqtime <- simlist$totqtime + simlist$currtime - qhead[3]
         simlist$nrepbusy <- simlist$nrepbusy + 1
         srvduration <- rexp(1,simlist$reprate)
         schedevnt(simlist,simlist$currtime+srvduration,simlist$repairevnt,
            qhead[3:4])
      } else {  # START NEW CODE:  take coffee break
         simlist$nrepbusy <- simlist$nrepbusy + 1
         schedevnt(simlist,simlist$currtime+0.1,simlist$coffevnt,
            appdata=c(NA,NA))
         # END NEW CODE
      }
   } else {  # new:  done with coffee break; any jobs waiting?
      simlist$nrepbusy <- simlist$nrepbusy - 1
      if (nrow(simlist$queue$m) > 0) {  
         qhead <- delfcfs(simlist$queue)
         simlist$totqtime <- simlist$totqtime + simlist$currtime - qhead[3]
         simlist$nrepbusy <- simlist$nrepbusy + 1
         srvduration <- rexp(1,simlist$reprate)
         schedevnt(simlist,simlist$currtime+srvduration,simlist$repairevnt,
            qhead[3:4])
      }
   }
}

source('DES.R')
mrp(5,1,10000,4,2)