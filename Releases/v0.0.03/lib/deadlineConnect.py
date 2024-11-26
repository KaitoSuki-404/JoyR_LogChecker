from Deadline.DeadlineConnect import DeadlineCon as Connect

class findPath:

    def __init__(self, ID:int, fileName:str, state:str = 'Failed'):
        self.joyID = str(ID)
        self.jobState = state
        self.logFile = fileName + ".log"
        self.deadlineHost = Connect('172.16.0.5', 8082)
        self.targetJobs = self.deadlineHost.Jobs.GetJobsInState(self.jobState)

    def findLogPath(self, pathList:list):
        # Get deadline jobID for the job
        # Due to heavy database, this stage may take 10 seconds or more
        for job in self.targetJobs:
            job = dict(job)

            # I'm using platform's special IDs to filter which jobID should we get
            # Recursions are required for this session
            # Maybe some other days I'll upgrade it with backend's apis
            jobOutDir = job.get('OutDir')
            for path in jobOutDir:
                if self.joyID in path:
                    jobID = job.get('_id')
                    # Return target jobID
                    targetJob = dict(self.deadlineHost.Jobs.GetJob(jobID))
                    jobProp = targetJob.get('Props')
                    pretaskScriptPath = jobProp.__getitem__('PrTskScrp')
                    secPath = pretaskScriptPath.replace(path, '').strip('.py')
                    # Return "\000000"

                    targetPath = path + "\logFiles" + secPath + self.logFile
                    # Return log file path
                    # \\172.16.0.16\Administrator\video\1856265513284018178\1108\1860571335101026305\logFiles\173128\0_501-501.log
                    pathList.append(targetPath)