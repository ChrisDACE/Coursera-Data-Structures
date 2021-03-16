# python3

# from collections import namedtuple
#
# AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])

class JobQueue:
    def __init__(self):
        self.n_workers, self.n_jobs = map(int, input().split())
        self.jobs = list(map(int, input().split()))
        assert len(self.jobs) == self.n_jobs

        self.assigned_workers = [-1] * self.n_jobs
        self.start_time = [-1] * self.n_jobs
        #self.next_available = [(0, i) for i in range(self.n_workers)]

    def sift_down(self, q, i):
        l = 2 * i + 1
        r = 2 * i + 2
        m = i

        if l < self.n_workers and (q[l][0] < q[m][0] or (q[l][0] == q[m][0] and q[l][1] < q[m][1])):
            m = l
        if r < self.n_workers and (q[r][0] < q[m][0] or (q[r][0] == q[m][0] and q[r][1] < q[m][1])):
            m = r

        if i != m:
            q[i], q[m] = q[m], q[i]
            self.sift_down(q, m)

    def assign_jobs(self):
        next_available = [(0, i) for i in range(self.n_workers)]
        for i in range(self.n_jobs):
            self.assigned_workers[i] = next_available[0][1]
            self.start_time[i] = next_available[0][0]
            next_available[0] = (next_available[0][0]+self.jobs[i], next_available[0][1])

            self.sift_down(next_available, 0)

    def solve(self):
        self.assign_jobs()
        for i in range(self.n_jobs):
            print(self.assigned_workers[i], self.start_time[i])


def main():
    solver = JobQueue()
    solver.solve()


if __name__ == "__main__":
    main()




# def assign_jobs(n_workers, jobs):

# # TODO: replace this code with a faster algorithm.
# result = []
# next_free_time = [0] * n_workers
# for job in jobs:
#     next_worker = min(range(n_workers), key=lambda w: next_free_time[w])
#     result.append(AssignedJob(next_worker, next_free_time[next_worker]))
#     next_free_time[next_worker] += job
#
# return result


# def main():
#     n_workers, n_jobs = map(int, input().split())
#     jobs = list(map(int, input().split()))
#     assert len(jobs) == n_jobs
#
#     assigned_jobs = assign_jobs(n_workers, jobs)
#
#     for job in assigned_jobs:
#         print(job.worker, job.started_at)


# if __name__ == "__main__":
#     main()
