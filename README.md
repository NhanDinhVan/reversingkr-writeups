# Reversing.kr Write-ups

This repository documents my learning journey in malware analysis and reverse engineering through hands-on practice on the Reversing.kr platform.

The goal of this project is not only to solve challenges, but also to build a well-structured public record of my reasoning process, tooling, and lessons learned along the way. Each write-up is intended to be clear enough for others to follow and useful enough for me to revisit later.

## Purpose

- Practice reverse engineering in a structured way.
- Record my analysis process instead of only posting final answers.
- Build a clean technical portfolio around malware analysis and reversing.
- Share notes, mistakes, and solutions that may help other beginners.

## Learning Environment

My main machine runs Ubuntu, but I do not perform malware analysis work directly on the host operating system. For this kind of practice, isolation matters. Reverse engineering often requires running unfamiliar executables, unpacking protected samples, inspecting suspicious behavior, and testing tools that are better supported on Windows. Doing that work on the host would be unnecessarily risky and harder to manage.

For that reason, I use a dedicated Windows lab inside a virtual machine. This gives me a controlled environment where I can experiment more freely, keep my daily system separated from the analysis workflow, and reset or rebuild the lab more easily when needed.

### Lab Setup

- **Host OS — Ubuntu Linux**  
  Ubuntu is my main working environment; I keep it outside the malware analysis lab to avoid risking the host and to store notes and VM images separately.

- **Virtualization — VirtualBox**  
  VirtualBox isolates the analysis environment, supports snapshots and easy reverts, and prevents analysis tools or samples from polluting the host.

- **Guest OS — Windows 10 Pro**  
  Many reversing tools and target binaries are Windows-specific. Using a Windows guest reduces friction for dynamic debugging, unpacking, and behavior tracing.

- **Convenience tools — VirtualBox Guest Additions**  
  Guest Additions improves clipboard sharing, screen resizing, and file transfer between host and guest, making the workflow smoother when moving files and screenshots.

- **Analysis toolkit — FLARE-VM**  
  FLARE-VM provides a prebuilt collection of reversing and malware analysis utilities so I can start experiments quickly with a standardized toolset.

Overall, this setup helps me balance safety, convenience, and realism. Ubuntu remains clean as the host platform, while the Windows virtual machine acts as the disposable analysis lab where I can install tools, run binaries, capture screenshots, and document the reversing process with less risk and better reproducibility.

> Suggested screenshot to add here:
> - VirtualBox manager showing the Windows 10 analysis VM
> - Windows 10 guest desktop after initial setup
> - FLARE-VM installation result or desktop/start menu with installed tools visible

## Repository Structure

```text
.
├── README.md
├── challenge-writeups/
│   ├── easy-crack/
│   │   └── image-evidences/
|   |   └── write-up.md
│   └── easy-unpack/
└── tools-and-enviroments/
```

### Folder Notes

- `challenge-writeups/`: Contains individual challenge solutions and analysis notes.
- `image-evidences/`: Stores screenshots or visual evidence used in a write-up.
- `tools-and-enviroments/`: Reserved for setup notes, tool installation records, and environment documentation.

## Write-up Style

I want each challenge write-up in this repository to follow a consistent structure:

1. Challenge overview
2. Initial observations
3. Tooling used
4. Step-by-step analysis
5. Key findings
6. Final solution
7. Lessons learned

Where useful, I will also include screenshots, debugger views, strings output, disassembly snippets, and short reflections on what I misunderstood during the process.


## References

- Reversing.kr
- Malware Analysis Fundamentals (Udemy): https://www.udemy.com/course/malware-analysis-fundamentals/

## Notes

This repository is a living study log. Some write-ups may start simple, but I plan to improve the quality, depth, and structure over time as my reversing skills grow.

If you find mistakes or have suggestions for better analysis methods, cleaner write-up structure, or better tooling practices, feedback is welcome.