# Claude Skills Library


**520 ready-to-use skills for Claude** across 45 categories: decision-making, coding, gym and fitness, productivity, life, writing, learning, game dev, business, research, and AI/meta work.

Each skill is a folder with a `SKILL.md` (YAML frontmatter + instructions) that follows the open Agent Skills format. Claude loads a skill automatically when your request matches its description.

## Quick start

### Claude.ai / Claude Desktop
1. Zip a single skill folder (for example `skills/02-coding/code-review/`) so the folder is the zip root.
2. Go to **Settings > Capabilities > Skills** and upload the zip.
3. Toggle it on and just ask naturally, e.g. "review this code" or "help me decide between these two options".

You can also run `./scripts/package_all.sh` to create one zip per skill in `dist/`.

### Claude Code
```bash
# all skills, available in every project
./scripts/install.sh --user

# or only for the current project
./scripts/install.sh --project
```
This copies skills into `~/.claude/skills/` or `./.claude/skills/`.

## Skill index

### Decision Making (`skills/01-decision-making/`)

Frameworks for choosing well under uncertainty, from quick gut-checks to big irreversible calls.

| Skill | What it does |
|---|---|
| [`decision-matrix`](skills/01-decision-making/decision-matrix/SKILL.md) | Build a weighted decision matrix to compare options against criteria. |
| [`pre-mortem`](skills/01-decision-making/pre-mortem/SKILL.md) | Run a pre-mortem: assume the plan already failed and work backwards to find why. |
| [`two-way-door`](skills/01-decision-making/two-way-door/SKILL.md) | Classify a decision as reversible (two-way door) or irreversible (one-way door) and set the right amount of deliberation. |
| [`second-order-thinking`](skills/01-decision-making/second-order-thinking/SKILL.md) | Trace consequences of a decision beyond the immediate effect: second and third-order impacts, feedback loops, and incentives. |
| [`devils-advocate`](skills/01-decision-making/devils-advocate/SKILL.md) | Argue the strongest case against the user's idea, plan, or belief to test it. |
| [`bias-check`](skills/01-decision-making/bias-check/SKILL.md) | Audit a decision or argument for cognitive biases (sunk cost, confirmation, anchoring, survivorship, overconfidence, planning fallacy, loss aversion, availability). |
| [`first-principles`](skills/01-decision-making/first-principles/SKILL.md) | Break a problem down to fundamental truths and rebuild solutions from scratch instead of by analogy. |
| [`big-life-decision`](skills/01-decision-making/big-life-decision/SKILL.md) | Guide a high-stakes personal decision (moving, quitting, relationships, school, big purchases) with values clarification, regret minimization, and small experiments. |
| [`opportunity-cost`](skills/01-decision-making/opportunity-cost/SKILL.md) | Make the hidden cost of a choice explicit: what else the money, time, or attention could buy. |
| [`expected-value`](skills/01-decision-making/expected-value/SKILL.md) | Evaluate uncertain choices with probabilities, payoffs, and expected value, including asymmetric risks and ruin avoidance. |
| [`buy-vs-build`](skills/01-decision-making/buy-vs-build/SKILL.md) | Decide whether to buy, subscribe, use open source, or build something custom. |
| [`decision-journal`](skills/01-decision-making/decision-journal/SKILL.md) | Create and maintain a decision journal entry that records the decision, reasoning, expectations, and confidence so outcomes can be reviewed later. |

### Coding (`skills/02-coding/`)

Engineering workflows: reviewing, debugging, testing, shipping, and building apps and games.

| Skill | What it does |
|---|---|
| [`code-review`](skills/02-coding/code-review/SKILL.md) | Perform a structured, prioritized code review covering correctness, security, performance, readability, and tests. |
| [`debug-protocol`](skills/02-coding/debug-protocol/SKILL.md) | Systematic debugging: reproduce, isolate, hypothesize, test, fix, and prevent regressions. |
| [`refactor-safely`](skills/02-coding/refactor-safely/SKILL.md) | Refactor code in small, behavior-preserving steps with tests as a safety net. |
| [`test-writer`](skills/02-coding/test-writer/SKILL.md) | Write thorough, maintainable tests (unit, integration, property-based) with good names, edge cases, and minimal mocking. |
| [`git-commit-pr`](skills/02-coding/git-commit-pr/SKILL.md) | Write clean commit messages, branch strategy, and pull request descriptions, and fix common git messes. |
| [`api-design`](skills/02-coding/api-design/SKILL.md) | Design clean REST, GraphQL, or RPC APIs with consistent naming, versioning, pagination, errors, auth, and idempotency. |
| [`sql-optimizer`](skills/02-coding/sql-optimizer/SKILL.md) | Write, explain, and optimize SQL queries and schemas: indexes, joins, EXPLAIN plans, N+1 problems. |
| [`security-audit`](skills/02-coding/security-audit/SKILL.md) | Audit code and architecture for common vulnerabilities (OWASP Top 10, secrets, authz, injection, SSRF, unsafe deserialization, dependency risk) and recommend defensive fixes. |
| [`performance-profiling`](skills/02-coding/performance-profiling/SKILL.md) | Find and fix performance bottlenecks using measurement: profiling, benchmarks, algorithmic analysis, caching, and memory. |
| [`adr-writer`](skills/02-coding/adr-writer/SKILL.md) | Write Architecture Decision Records capturing context, options, decision, and consequences. |
| [`regex-builder`](skills/02-coding/regex-builder/SKILL.md) | Build, explain, and test regular expressions with examples and edge cases. |
| [`readme-writer`](skills/02-coding/readme-writer/SKILL.md) | Write clear, attractive README files and project docs: purpose, quickstart, usage, configuration, contributing, license. |
| [`dependency-upgrade`](skills/02-coding/dependency-upgrade/SKILL.md) | Plan and execute dependency and framework upgrades safely: changelog review, breaking changes, codemods, staged rollout. |
| [`error-handling`](skills/02-coding/error-handling/SKILL.md) | Design robust error handling, validation, retries, timeouts, and logging. |
| [`code-explainer`](skills/02-coding/code-explainer/SKILL.md) | Explain unfamiliar code clearly at the user's level, with a walkthrough, data flow, and diagrams. |
| [`shell-scripting`](skills/02-coding/shell-scripting/SKILL.md) | Write safe, portable bash/zsh scripts and one-liners with error handling and clear usage. |
| [`docker-setup`](skills/02-coding/docker-setup/SKILL.md) | Create Dockerfiles, docker-compose setups, and dev containers with small images, caching, healthchecks, and security. |
| [`ci-cd-pipeline`](skills/02-coding/ci-cd-pipeline/SKILL.md) | Design CI/CD pipelines (GitHub Actions, GitLab CI) with lint, test, build, cache, release, and deploy stages. |
| [`database-schema-design`](skills/02-coding/database-schema-design/SKILL.md) | Design relational and document schemas with proper normalization, keys, constraints, indexes, and migrations. |
| [`tech-debt-triage`](skills/02-coding/tech-debt-triage/SKILL.md) | Inventory and prioritize technical debt by impact, effort, and risk, and turn it into an actionable plan. |
| [`algorithm-solver`](skills/02-coding/algorithm-solver/SKILL.md) | Solve algorithm and data-structure problems with problem restatement, approach comparison, complexity, and clean code. |
| [`godot-gdscript`](skills/02-coding/godot-gdscript/SKILL.md) | Build Godot 4 games with GDScript: scene architecture, signals, autoloads, resources, physics, input, multiplayer, and performance. |
| [`electron-app`](skills/02-coding/electron-app/SKILL.md) | Build desktop apps with Electron: main/renderer architecture, IPC, security, packaging, auto-update. |
| [`swift-macos-app`](skills/02-coding/swift-macos-app/SKILL.md) | Build native macOS apps in Swift/SwiftUI/AppKit: menu bar apps, windows, drag-and-drop, notch UI, sandboxing, and distribution. |
| [`web-scraper-builder`](skills/02-coding/web-scraper-builder/SKILL.md) | Design ethical, resilient web scrapers and data collectors: HTTP vs. |
| [`single-file-html-game`](skills/02-coding/single-file-html-game/SKILL.md) | Build complete browser games in one HTML file with canvas, game loop, input, sprites, audio, and save data. |
| [`logging-observability`](skills/02-coding/logging-observability/SKILL.md) | Add structured logging, metrics, tracing, and alerts so systems are debuggable in production. |
| [`code-migration`](skills/02-coding/code-migration/SKILL.md) | Migrate code between languages, frameworks, or versions (JS to TS, Python 2 to 3, REST to GraphQL, Godot 3 to 4) with parity checks. |

### Gym & Fitness (`skills/03-gym-fitness/`)

Training, programming, and activity planning.

| Skill | What it does |
|---|---|
| [`workout-program-designer`](skills/03-gym-fitness/workout-program-designer/SKILL.md) | Design a personalized strength or hypertrophy training program with splits, exercise selection, sets, reps, and progression. |
| [`progressive-overload-tracker`](skills/03-gym-fitness/progressive-overload-tracker/SKILL.md) | Track lifts and recommend when and how much to increase weight, reps, or sets based on logged performance. |
| [`exercise-form-guide`](skills/03-gym-fitness/exercise-form-guide/SKILL.md) | Explain exercise technique with setup, execution cues, common mistakes, and regressions/progressions. |
| [`mobility-and-warmup`](skills/03-gym-fitness/mobility-and-warmup/SKILL.md) | Build warm-ups, mobility routines, and stretching sequences tailored to a workout or problem area. |
| [`deload-and-recovery-planner`](skills/03-gym-fitness/deload-and-recovery-planner/SKILL.md) | Plan deloads, rest days, sleep, and recovery strategies when training fatigue builds. |
| [`home-gym-planner`](skills/03-gym-fitness/home-gym-planner/SKILL.md) | Plan a home gym by budget and space: equipment priorities, used-gear tips, layout, and programs for what you own. |
| [`running-plan`](skills/03-gym-fitness/running-plan/SKILL.md) | Create beginner-to-intermediate running plans (5K, 10K, half marathon) with easy/long/interval runs, walk breaks, and strength work. |
| [`workout-log-analyzer`](skills/03-gym-fitness/workout-log-analyzer/SKILL.md) | Analyze workout history for volume, frequency, balance, and trends, and suggest adjustments. |
| [`calisthenics-progressions`](skills/03-gym-fitness/calisthenics-progressions/SKILL.md) | Plan bodyweight training progressions toward pull-ups, push-ups, dips, handstands, and muscle-ups. |

### Productivity (`skills/04-productivity/`)

Planning, focus, reviews, and getting things done without burning out.

| Skill | What it does |
|---|---|
| [`weekly-review`](skills/04-productivity/weekly-review/SKILL.md) | Run a structured weekly review: wins, lessons, open loops, next week's priorities. |
| [`daily-planner`](skills/04-productivity/daily-planner/SKILL.md) | Build a realistic daily plan from tasks, energy, and calendar, with time blocks and buffers. |
| [`eisenhower-prioritizer`](skills/04-productivity/eisenhower-prioritizer/SKILL.md) | Sort tasks by urgency and importance and decide what to do, schedule, delegate, or delete. |
| [`goal-setting-okr`](skills/04-productivity/goal-setting-okr/SKILL.md) | Turn ambitions into clear goals with OKRs or SMART milestones and weekly actions. |
| [`habit-builder`](skills/04-productivity/habit-builder/SKILL.md) | Design habits using cues, tiny starts, environment design, and tracking. |
| [`deep-work-session`](skills/04-productivity/deep-work-session/SKILL.md) | Set up and run a focused deep-work session: goal, distraction blocking, timers, and review. |
| [`meeting-notes`](skills/04-productivity/meeting-notes/SKILL.md) | Turn raw meeting notes or transcripts into decisions, action items, owners, and deadlines. |
| [`project-breakdown`](skills/04-productivity/project-breakdown/SKILL.md) | Break a big project into milestones, tasks, dependencies, estimates, and a first-week plan. |
| [`time-audit`](skills/04-productivity/time-audit/SKILL.md) | Audit how time is spent, find leaks, and reallocate toward priorities. |
| [`email-writer`](skills/04-productivity/email-writer/SKILL.md) | Write clear, concise, tone-appropriate emails and replies for work, school, and negotiation. |

### Life (`skills/05-life/`)

Money, travel, career, and everyday life planning.

| Skill | What it does |
|---|---|
| [`budget-planner`](skills/05-life/budget-planner/SKILL.md) | Create a simple personal budget with needs/wants/savings, tracking categories, and goals. |
| [`travel-planner`](skills/05-life/travel-planner/SKILL.md) | Plan trips with itinerary, budget, logistics, and local tips tailored to preferences. |
| [`career-planner`](skills/05-life/career-planner/SKILL.md) | Plan career moves: skills gap analysis, resume positioning, networking, and 90-day plans. |
| [`interview-prep`](skills/05-life/interview-prep/SKILL.md) | Prepare for interviews with story banks (STAR), role research, questions to ask, and mock practice. |
| [`negotiation-coach`](skills/05-life/negotiation-coach/SKILL.md) | Prepare for negotiations (salary, rent, purchases, contracts) with anchors, BATNA, and scripts. |
| [`buying-research`](skills/05-life/buying-research/SKILL.md) | Research purchases methodically: needs, shortlist, criteria, tradeoffs, and where to buy. |
| [`home-project-planner`](skills/05-life/home-project-planner/SKILL.md) | Plan DIY and home projects with materials, tools, steps, safety, and budget. |
| [`meal-planner`](skills/05-life/meal-planner/SKILL.md) | Create weekly meal plans and shopping lists around taste, time, budget, and dietary needs. |
| [`pet-care-helper`](skills/05-life/pet-care-helper/SKILL.md) | Provide pet care guidance: training basics, routines, and enrichment for dogs and cats. |

### Writing (`skills/06-writing/`)

Drafting, editing, and communicating clearly.

| Skill | What it does |
|---|---|
| [`editor`](skills/06-writing/editor/SKILL.md) | Edit writing for clarity, concision, structure, and tone while keeping the author's voice. |
| [`voice-matcher`](skills/06-writing/voice-matcher/SKILL.md) | Learn a writing voice from samples and write new text in that voice. |
| [`summarizer`](skills/06-writing/summarizer/SKILL.md) | Summarize documents, articles, threads, or transcripts at multiple lengths with key points and action items. |
| [`outline-builder`](skills/06-writing/outline-builder/SKILL.md) | Create strong outlines for essays, articles, talks, and reports with a clear thesis and flow. |
| [`headline-and-hook`](skills/06-writing/headline-and-hook/SKILL.md) | Generate headlines, titles, subject lines, and opening hooks with variations and tests. |
| [`technical-writing`](skills/06-writing/technical-writing/SKILL.md) | Write clear technical documentation, tutorials, how-to guides, and API docs. |
| [`storytelling`](skills/06-writing/storytelling/SKILL.md) | Craft compelling stories for presentations, brands, and fiction using structure, stakes, and specific detail. |

### Learning (`skills/07-learning/`)

Learn faster and retain more.

| Skill | What it does |
|---|---|
| [`feynman-explainer`](skills/07-learning/feynman-explainer/SKILL.md) | Explain any concept simply using the Feynman technique: plain language, analogies, and gap-finding. |
| [`flashcard-maker`](skills/07-learning/flashcard-maker/SKILL.md) | Create effective spaced-repetition flashcards (Anki-style) from notes, text, or topics. |
| [`study-plan`](skills/07-learning/study-plan/SKILL.md) | Build a study plan with milestones, spaced practice, and active recall for exams or skills. |
| [`socratic-tutor`](skills/07-learning/socratic-tutor/SKILL.md) | Teach by asking guiding questions instead of giving answers, adapting to the learner. |
| [`reading-notes`](skills/07-learning/reading-notes/SKILL.md) | Extract and organize notes from books, papers, and articles into insights, quotes, and action items. |
| [`language-learning`](skills/07-learning/language-learning/SKILL.md) | Coach language learning with vocabulary, grammar, speaking practice, and daily routines. |

### Creative & Game Dev (`skills/08-creative-gamedev/`)

Game design, worldbuilding, and creative production.

| Skill | What it does |
|---|---|
| [`game-design-doc`](skills/08-creative-gamedev/game-design-doc/SKILL.md) | Write a game design document: pillars, core loop, mechanics, progression, content, art direction, and scope. |
| [`game-balance`](skills/08-creative-gamedev/game-balance/SKILL.md) | Balance game economies, difficulty, progression curves, and drop rates with math and playtest plans. |
| [`level-design`](skills/08-creative-gamedev/level-design/SKILL.md) | Design levels and maps with pacing, teaching, flow, landmarks, and risk/reward. |
| [`worldbuilding`](skills/08-creative-gamedev/worldbuilding/SKILL.md) | Build coherent fictional worlds: geography, cultures, factions, history, and conflict. |
| [`character-creator`](skills/08-creative-gamedev/character-creator/SKILL.md) | Create memorable characters with motivations, flaws, voice, arcs, and relationships. |
| [`narrative-dialogue`](skills/08-creative-gamedev/narrative-dialogue/SKILL.md) | Write natural, character-driven dialogue and branching conversations for games and stories. |
| [`game-juice-polish`](skills/08-creative-gamedev/game-juice-polish/SKILL.md) | Add game feel and polish: screen shake, hit-stop, particles, easing, sound, UI feedback. |
| [`procedural-generation`](skills/08-creative-gamedev/procedural-generation/SKILL.md) | Design procedural generation: noise, wave function collapse, BSP dungeons, random tables, and seeded determinism. |
| [`shop-sim-economy`](skills/08-creative-gamedev/shop-sim-economy/SKILL.md) | Design shop and business-sim loops: customers, orders, upgrades, staff, and unlock curves. |
| [`pixel-art-spec`](skills/08-creative-gamedev/pixel-art-spec/SKILL.md) | Define pixel-art style guides: resolution, palette, tiles, animation frames, and tooling. |

### Business (`skills/09-business/`)

Validate ideas, price products, and reach customers.

| Skill | What it does |
|---|---|
| [`idea-validator`](skills/09-business/idea-validator/SKILL.md) | Validate a business or product idea with customer problem, market size, competition, and cheap tests. |
| [`lean-canvas`](skills/09-business/lean-canvas/SKILL.md) | Create a Lean Canvas: problem, solution, metrics, value prop, channels, revenue, costs, and advantage. |
| [`pricing-strategy`](skills/09-business/pricing-strategy/SKILL.md) | Set pricing using value, costs, competitors, and psychology, with tiers and tests. |
| [`competitor-analysis`](skills/09-business/competitor-analysis/SKILL.md) | Analyze competitors' products, positioning, pricing, and gaps. |
| [`landing-page-copy`](skills/09-business/landing-page-copy/SKILL.md) | Write high-converting landing page copy: headline, benefits, proof, objections, and calls to action. |
| [`cold-outreach`](skills/09-business/cold-outreach/SKILL.md) | Write personalized outreach messages and follow-up sequences that respect the recipient. |
| [`customer-interview`](skills/09-business/customer-interview/SKILL.md) | Plan and analyze customer discovery interviews using past-behavior questions. |
| [`resale-flip-analyzer`](skills/09-business/resale-flip-analyzer/SKILL.md) | Analyze resale opportunities for watches, sneakers, electronics, and collectibles: sourcing price, fees, shipping, comps, and margin. |
| [`financial-model-basics`](skills/09-business/financial-model-basics/SKILL.md) | Build simple financial models: revenue, costs, margins, runway, and break-even. |

### Research & Analysis (`skills/10-research-and-analysis/`)

Evaluate evidence and turn data into conclusions.

| Skill | What it does |
|---|---|
| [`fact-check`](skills/10-research-and-analysis/fact-check/SKILL.md) | Verify claims systematically by checking sources, dates, context, and consensus. |
| [`source-evaluator`](skills/10-research-and-analysis/source-evaluator/SKILL.md) | Assess source credibility: author, evidence, bias, recency, and corroboration. |
| [`data-analysis-plan`](skills/10-research-and-analysis/data-analysis-plan/SKILL.md) | Plan data analysis: question, data, cleaning, methods, visualization, and caveats. |
| [`compare-options-report`](skills/10-research-and-analysis/compare-options-report/SKILL.md) | Produce a clear comparison report of options with criteria, evidence, and a recommendation. |
| [`literature-review`](skills/10-research-and-analysis/literature-review/SKILL.md) | Structure a literature review: scope, search strategy, themes, gaps, and synthesis. |

### Meta & AI (`skills/11-meta-and-ai/`)

Skills for building with Claude and other AI tools.

| Skill | What it does |
|---|---|
| [`skill-builder`](skills/11-meta-and-ai/skill-builder/SKILL.md) | Design and write new Claude skills: purpose, trigger description, instructions, resources, and tests. |
| [`prompt-engineer`](skills/11-meta-and-ai/prompt-engineer/SKILL.md) | Write and improve prompts using clear context, examples, constraints, and output formats. |
| [`claude-md-writer`](skills/11-meta-and-ai/claude-md-writer/SKILL.md) | Write CLAUDE.md or project instruction files so coding agents understand the repo: commands, architecture, conventions. |
| [`agent-workflow-designer`](skills/11-meta-and-ai/agent-workflow-designer/SKILL.md) | Design multi-step AI agent workflows: tools, memory, guardrails, evals, and human checkpoints. |
| [`mcp-server-planner`](skills/11-meta-and-ai/mcp-server-planner/SKILL.md) | Plan and scaffold MCP servers: tools, resources, schemas, auth, and testing. |

### DevOps & Cloud (`skills/12-devops-and-cloud/`)

Infrastructure, deployment, reliability, and running systems in production.

| Skill | What it does |
|---|---|
| [`terraform-iac`](skills/12-devops-and-cloud/terraform-iac/SKILL.md) | Write and review Terraform/OpenTofu infrastructure as code with modules, remote state, and safe applies. |
| [`kubernetes-manifests`](skills/12-devops-and-cloud/kubernetes-manifests/SKILL.md) | Write and debug Kubernetes manifests: Deployments, Services, Ingress, ConfigMaps, probes, and resource limits. |
| [`helm-charts`](skills/12-devops-and-cloud/helm-charts/SKILL.md) | Create and maintain Helm charts with templated values, helpers, and environment overrides. |
| [`aws-architecture`](skills/12-devops-and-cloud/aws-architecture/SKILL.md) | Design AWS architectures for web apps, APIs, data pipelines, and event systems with sensible service choices. |
| [`cloud-cost-optimizer`](skills/12-devops-and-cloud/cloud-cost-optimizer/SKILL.md) | Reduce cloud spend by right-sizing, reserved capacity, storage tiers, and removing waste. |
| [`linux-sysadmin`](skills/12-devops-and-cloud/linux-sysadmin/SKILL.md) | Administer Linux servers: users, permissions, systemd, networking, disk, logs, and hardening basics. |
| [`nginx-config`](skills/12-devops-and-cloud/nginx-config/SKILL.md) | Write and debug nginx configs: reverse proxy, TLS, caching, rate limits, and static hosting. |
| [`incident-response`](skills/12-devops-and-cloud/incident-response/SKILL.md) | Run a production incident: triage, mitigate, communicate, and recover. |
| [`postmortem-writer`](skills/12-devops-and-cloud/postmortem-writer/SKILL.md) | Write blameless postmortems with timeline, root cause, impact, and action items. |
| [`runbook-writer`](skills/12-devops-and-cloud/runbook-writer/SKILL.md) | Create operational runbooks with symptoms, diagnosis steps, commands, and escalation paths. |
| [`slo-designer`](skills/12-devops-and-cloud/slo-designer/SKILL.md) | Define SLIs, SLOs, and error budgets for services. |
| [`deployment-strategies`](skills/12-devops-and-cloud/deployment-strategies/SKILL.md) | Choose and implement deployment strategies: rolling, blue/green, canary, and feature flags. |
| [`secrets-management`](skills/12-devops-and-cloud/secrets-management/SKILL.md) | Manage secrets safely with vaults, environment variables, rotation, and scanning. |
| [`backup-and-recovery`](skills/12-devops-and-cloud/backup-and-recovery/SKILL.md) | Design backup and disaster-recovery plans with RPO/RTO, testing, and offsite copies. |
| [`load-testing`](skills/12-devops-and-cloud/load-testing/SKILL.md) | Plan and run load tests with k6, Locust, or JMeter and interpret results. |
| [`serverless-design`](skills/12-devops-and-cloud/serverless-design/SKILL.md) | Design serverless apps with Lambda or Cloud Functions, queues, and managed services. |
| [`self-hosting-homelab`](skills/12-devops-and-cloud/self-hosting-homelab/SKILL.md) | Plan self-hosted services and homelabs with Docker, reverse proxies, DNS, VPN, and backups. |

### Data & Machine Learning (`skills/13-data-and-ml/`)

Data wrangling, analytics, statistics, and machine learning workflows.

| Skill | What it does |
|---|---|
| [`pandas-wrangling`](skills/13-data-and-ml/pandas-wrangling/SKILL.md) | Clean, reshape, merge, and aggregate data with pandas or polars. |
| [`data-cleaning`](skills/13-data-and-ml/data-cleaning/SKILL.md) | Detect and fix data quality problems: duplicates, outliers, missing values, inconsistent formats. |
| [`exploratory-analysis`](skills/13-data-and-ml/exploratory-analysis/SKILL.md) | Run exploratory data analysis: distributions, relationships, segments, and anomalies. |
| [`sql-analytics-queries`](skills/13-data-and-ml/sql-analytics-queries/SKILL.md) | Write analytics SQL: window functions, cohorts, funnels, retention, and rolling metrics. |
| [`dashboard-design`](skills/13-data-and-ml/dashboard-design/SKILL.md) | Design clear dashboards with the right metrics, charts, and layout. |
| [`ab-test-designer`](skills/13-data-and-ml/ab-test-designer/SKILL.md) | Design and analyze A/B tests: hypothesis, sample size, metrics, duration, and significance. |
| [`statistics-explainer`](skills/13-data-and-ml/statistics-explainer/SKILL.md) | Explain statistical concepts and pick the right test: p-values, confidence intervals, regression, Bayesian basics. |
| [`ml-model-selection`](skills/13-data-and-ml/ml-model-selection/SKILL.md) | Choose machine learning models and baselines for tabular, text, image, or time-series problems. |
| [`feature-engineering`](skills/13-data-and-ml/feature-engineering/SKILL.md) | Create and select features that improve models: encoding, scaling, interactions, and time features. |
| [`model-evaluation`](skills/13-data-and-ml/model-evaluation/SKILL.md) | Evaluate models with proper splits, metrics, calibration, and error analysis. |
| [`pytorch-training-loop`](skills/13-data-and-ml/pytorch-training-loop/SKILL.md) | Write and debug PyTorch training loops, datasets, and GPU usage. |
| [`time-series-forecasting`](skills/13-data-and-ml/time-series-forecasting/SKILL.md) | Forecast time series with baselines, seasonality, and models like ARIMA, Prophet, or gradient boosting. |
| [`data-viz-chooser`](skills/13-data-and-ml/data-viz-chooser/SKILL.md) | Pick the right chart and design it honestly: comparisons, trends, distributions, relationships. |
| [`etl-pipeline-design`](skills/13-data-and-ml/etl-pipeline-design/SKILL.md) | Design reliable ETL/ELT pipelines with idempotency, schema checks, and orchestration. |
| [`data-warehouse-modeling`](skills/13-data-and-ml/data-warehouse-modeling/SKILL.md) | Model warehouses with star schemas, dimensions, facts, and slowly changing dimensions. |
| [`notebook-to-production`](skills/13-data-and-ml/notebook-to-production/SKILL.md) | Turn notebooks into maintainable, tested, deployable code. |

### Frontend & Web (`skills/14-frontend-web/`)

Building fast, accessible, good-looking web interfaces.

| Skill | What it does |
|---|---|
| [`react-components`](skills/14-frontend-web/react-components/SKILL.md) | Build clean React components with props, composition, and hooks. |
| [`react-hooks-patterns`](skills/14-frontend-web/react-hooks-patterns/SKILL.md) | Use React hooks correctly: useEffect pitfalls, custom hooks, memoization, and data fetching. |
| [`state-management`](skills/14-frontend-web/state-management/SKILL.md) | Choose and structure state management: local state, context, Redux, Zustand, or server-state libraries. |
| [`css-layout`](skills/14-frontend-web/css-layout/SKILL.md) | Solve CSS layout with flexbox, grid, and positioning. |
| [`tailwind-ui`](skills/14-frontend-web/tailwind-ui/SKILL.md) | Build polished interfaces with Tailwind CSS: spacing scale, responsive variants, dark mode, and components. |
| [`responsive-design`](skills/14-frontend-web/responsive-design/SKILL.md) | Make sites work across phones, tablets, and desktops with fluid layouts and breakpoints. |
| [`web-accessibility`](skills/14-frontend-web/web-accessibility/SKILL.md) | Audit and fix web accessibility: semantics, keyboard, contrast, ARIA, and screen readers against WCAG. |
| [`web-performance`](skills/14-frontend-web/web-performance/SKILL.md) | Improve web performance: Core Web Vitals, bundle size, images, caching, and rendering. |
| [`nextjs-app`](skills/14-frontend-web/nextjs-app/SKILL.md) | Build Next.js apps with the App Router, server components, routing, data fetching, and deployment. |
| [`typescript-types`](skills/14-frontend-web/typescript-types/SKILL.md) | Write precise TypeScript types: generics, unions, utility types, and narrowing. |
| [`form-validation`](skills/14-frontend-web/form-validation/SKILL.md) | Build robust forms with validation, errors, accessibility, and submission handling. |
| [`web-animation`](skills/14-frontend-web/web-animation/SKILL.md) | Create smooth web animations with CSS transitions, keyframes, and JS libraries. |
| [`pwa-builder`](skills/14-frontend-web/pwa-builder/SKILL.md) | Turn a website into a Progressive Web App: manifest, service worker, offline, and install prompts. |
| [`browser-extension`](skills/14-frontend-web/browser-extension/SKILL.md) | Build browser extensions for Chrome and Firefox with Manifest V3: content scripts, background workers, and permissions. |
| [`design-tokens`](skills/14-frontend-web/design-tokens/SKILL.md) | Define and implement design tokens for color, type, spacing, and theming across web apps. |
| [`canvas-graphics`](skills/14-frontend-web/canvas-graphics/SKILL.md) | Draw and animate with HTML canvas and WebGL: render loops, sprites, particles, and hit-testing. |
| [`threejs-scene`](skills/14-frontend-web/threejs-scene/SKILL.md) | Build 3D web scenes with three.js: cameras, lights, materials, models, and animation. |
| [`charts-d3`](skills/14-frontend-web/charts-d3/SKILL.md) | Build custom data visualizations with D3 or Chart.js: scales, axes, transitions, and interaction. |

### Languages & Backend (`skills/15-languages-and-backend/`)

Language-specific coaching and backend engineering patterns.

| Skill | What it does |
|---|---|
| [`python-best-practices`](skills/15-languages-and-backend/python-best-practices/SKILL.md) | Write idiomatic, typed, tested Python: packaging, virtualenvs, dataclasses, async, and tooling. |
| [`rust-ownership-coach`](skills/15-languages-and-backend/rust-ownership-coach/SKILL.md) | Teach and debug Rust: ownership, borrowing, lifetimes, traits, and error handling. |
| [`go-concurrency`](skills/15-languages-and-backend/go-concurrency/SKILL.md) | Write Go with goroutines, channels, contexts, and worker pools safely. |
| [`node-typescript-api`](skills/15-languages-and-backend/node-typescript-api/SKILL.md) | Build Node.js APIs in TypeScript with Express or Fastify, validation, middleware, and testing. |
| [`java-spring-boot`](skills/15-languages-and-backend/java-spring-boot/SKILL.md) | Build Spring Boot services: controllers, JPA, config, security, and testing. |
| [`csharp-dotnet`](skills/15-languages-and-backend/csharp-dotnet/SKILL.md) | Write modern C# and .NET: ASP.NET Core, LINQ, async/await, dependency injection, and EF Core. |
| [`cpp-modern`](skills/15-languages-and-backend/cpp-modern/SKILL.md) | Write modern C++ (17/20): RAII, smart pointers, templates, STL, and build tooling. |
| [`swift-language`](skills/15-languages-and-backend/swift-language/SKILL.md) | Write idiomatic Swift: optionals, protocols, value types, concurrency with async/await and actors. |
| [`lua-scripting`](skills/15-languages-and-backend/lua-scripting/SKILL.md) | Write Lua for games and tools: tables, metatables, coroutines, and embedding. |
| [`php-laravel`](skills/15-languages-and-backend/php-laravel/SKILL.md) | Build PHP apps with Laravel: routing, Eloquent, queues, validation, and testing. |
| [`ruby-on-rails`](skills/15-languages-and-backend/ruby-on-rails/SKILL.md) | Build Rails apps following conventions: models, controllers, ActiveRecord, and testing. |
| [`elixir-otp`](skills/15-languages-and-backend/elixir-otp/SKILL.md) | Build fault-tolerant systems with Elixir, OTP, GenServers, and Phoenix. |
| [`graphql-server`](skills/15-languages-and-backend/graphql-server/SKILL.md) | Design and build GraphQL servers: schema, resolvers, dataloaders, auth, and pagination. |
| [`websocket-realtime`](skills/15-languages-and-backend/websocket-realtime/SKILL.md) | Build realtime features with WebSockets or SSE: presence, rooms, reconnection, and scaling. |
| [`queues-and-workers`](skills/15-languages-and-backend/queues-and-workers/SKILL.md) | Design background jobs with queues, retries, dead letters, and idempotency. |
| [`caching-strategy`](skills/15-languages-and-backend/caching-strategy/SKILL.md) | Design caching: browser, CDN, application, and database layers with invalidation. |
| [`auth-implementation`](skills/15-languages-and-backend/auth-implementation/SKILL.md) | Implement authentication and authorization: sessions, JWT, OAuth/OIDC, passwords, and roles. |
| [`design-patterns`](skills/15-languages-and-backend/design-patterns/SKILL.md) | Apply software design patterns appropriately: strategy, observer, factory, adapter, and more. |
| [`clean-architecture`](skills/15-languages-and-backend/clean-architecture/SKILL.md) | Structure applications with layers, ports and adapters, and clear dependency direction. |
| [`monolith-vs-microservices`](skills/15-languages-and-backend/monolith-vs-microservices/SKILL.md) | Decide between monolith, modular monolith, and microservices based on team and scale. |

### Design & UX (`skills/16-design-and-ux/`)

Visual design, interaction design, and user research.

| Skill | What it does |
|---|---|
| [`ux-heuristic-review`](skills/16-design-and-ux/ux-heuristic-review/SKILL.md) | Review interfaces with Nielsen's usability heuristics and report issues by severity. |
| [`user-flow-mapper`](skills/16-design-and-ux/user-flow-mapper/SKILL.md) | Map user flows and journeys with steps, decisions, and edge cases. |
| [`wireframe-spec`](skills/16-design-and-ux/wireframe-spec/SKILL.md) | Describe wireframes for screens with layout, components, content, and states. |
| [`color-palette-builder`](skills/16-design-and-ux/color-palette-builder/SKILL.md) | Create accessible color palettes with contrast checks, scales, and usage rules. |
| [`typography-system`](skills/16-design-and-ux/typography-system/SKILL.md) | Select and pair fonts and define a type scale and hierarchy. |
| [`logo-brief`](skills/16-design-and-ux/logo-brief/SKILL.md) | Write brand and logo design briefs and critique concepts. |
| [`app-icon-and-assets`](skills/16-design-and-ux/app-icon-and-assets/SKILL.md) | Plan app icons, splash screens, and asset sets with sizes and platform guidelines. |
| [`design-critique`](skills/16-design-and-ux/design-critique/SKILL.md) | Give constructive visual design critique on hierarchy, spacing, alignment, and consistency. |
| [`microcopy-writer`](skills/16-design-and-ux/microcopy-writer/SKILL.md) | Write UI microcopy: buttons, errors, empty states, tooltips, and onboarding. |
| [`onboarding-flow`](skills/16-design-and-ux/onboarding-flow/SKILL.md) | Design onboarding that gets users to their first success fast. |
| [`usability-test-plan`](skills/16-design-and-ux/usability-test-plan/SKILL.md) | Plan and run usability tests: tasks, script, participants, and analysis. |
| [`design-system-docs`](skills/16-design-and-ux/design-system-docs/SKILL.md) | Document design system components with usage, variants, states, and accessibility. |

### Marketing & Growth (`skills/17-marketing-and-growth/`)

Content, SEO, social, email, and growth experiments.

| Skill | What it does |
|---|---|
| [`seo-content-strategy`](skills/17-marketing-and-growth/seo-content-strategy/SKILL.md) | Plan SEO content with keyword research, intent mapping, topic clusters, and briefs. |
| [`blog-post-writer`](skills/17-marketing-and-growth/blog-post-writer/SKILL.md) | Write engaging blog posts with strong structure, examples, and calls to action. |
| [`social-media-planner`](skills/17-marketing-and-growth/social-media-planner/SKILL.md) | Plan social media content calendars with formats, hooks, and posting cadence for each platform. |
| [`email-newsletter`](skills/17-marketing-and-growth/email-newsletter/SKILL.md) | Write and structure email newsletters and drip sequences with strong subject lines. |
| [`youtube-strategy`](skills/17-marketing-and-growth/youtube-strategy/SKILL.md) | Plan YouTube channels and videos: niche, titles, thumbnails, hooks, and retention. |
| [`tiktok-short-form`](skills/17-marketing-and-growth/tiktok-short-form/SKILL.md) | Create short-form video concepts with hooks, pacing, captions, and trends. |
| [`brand-positioning`](skills/17-marketing-and-growth/brand-positioning/SKILL.md) | Define brand positioning, voice, and messaging pillars. |
| [`ad-copy-writer`](skills/17-marketing-and-growth/ad-copy-writer/SKILL.md) | Write paid ad copy for search and social with variations and testing plans. |
| [`growth-experiments`](skills/17-marketing-and-growth/growth-experiments/SKILL.md) | Design growth experiments with hypotheses, ICE scoring, and learning loops. |
| [`product-hunt-launch`](skills/17-marketing-and-growth/product-hunt-launch/SKILL.md) | Plan a product launch on Product Hunt or similar: assets, timing, outreach, and follow-up. |
| [`content-repurposing`](skills/17-marketing-and-growth/content-repurposing/SKILL.md) | Turn one piece of content into many formats across channels. |
| [`press-release-writer`](skills/17-marketing-and-growth/press-release-writer/SKILL.md) | Write press releases and media pitches with strong news angles. |
| [`community-building`](skills/17-marketing-and-growth/community-building/SKILL.md) | Build and manage online communities on Discord, forums, or social. |
| [`customer-persona-builder`](skills/17-marketing-and-growth/customer-persona-builder/SKILL.md) | Create evidence-based customer personas and jobs-to-be-done. |

### Finance & Investing (`skills/18-finance-and-investing/`)

Educational frameworks for money, markets, and business finance.

| Skill | What it does |
|---|---|
| [`investing-basics`](skills/18-finance-and-investing/investing-basics/SKILL.md) | Explain investing fundamentals: index funds, diversification, risk, compounding, and fees. |
| [`compound-interest-calculator`](skills/18-finance-and-investing/compound-interest-calculator/SKILL.md) | Calculate compound growth, loan payoff, and savings goals with formulas and tables. |
| [`debt-payoff-planner`](skills/18-finance-and-investing/debt-payoff-planner/SKILL.md) | Compare avalanche and snowball debt payoff strategies with timelines. |
| [`stock-analysis-framework`](skills/18-finance-and-investing/stock-analysis-framework/SKILL.md) | Analyze companies with fundamentals: business model, margins, growth, valuation, and risks. |
| [`startup-financial-model`](skills/18-finance-and-investing/startup-financial-model/SKILL.md) | Build startup financial models: unit economics, CAC, LTV, burn, runway, and fundraising needs. |
| [`valuation-basics`](skills/18-finance-and-investing/valuation-basics/SKILL.md) | Explain valuation methods: DCF, multiples, and comparables for businesses. |
| [`tax-concepts-explainer`](skills/18-finance-and-investing/tax-concepts-explainer/SKILL.md) | Explain general tax concepts like deductions, credits, brackets, and business expenses. |
| [`freelancer-finances`](skills/18-finance-and-investing/freelancer-finances/SKILL.md) | Organize freelance and side-business finances: invoicing, quarterly set-asides, expenses, and rates. |
| [`rent-vs-buy-analysis`](skills/18-finance-and-investing/rent-vs-buy-analysis/SKILL.md) | Compare renting and buying a home with total cost, opportunity cost, and sensitivity. |
| [`expense-tracker-design`](skills/18-finance-and-investing/expense-tracker-design/SKILL.md) | Design simple expense tracking systems with categories, tools, and review habits. |
| [`crypto-concepts-explainer`](skills/18-finance-and-investing/crypto-concepts-explainer/SKILL.md) | Explain blockchain and crypto concepts, wallets, and risks neutrally. |
| [`pricing-unit-economics`](skills/18-finance-and-investing/pricing-unit-economics/SKILL.md) | Compute unit economics for products: COGS, margins, fees, and break-even volumes. |

### Sales & Customer Success (`skills/19-sales-and-customer/`)

Selling, supporting, and keeping customers.

| Skill | What it does |
|---|---|
| [`sales-discovery-call`](skills/19-sales-and-customer/sales-discovery-call/SKILL.md) | Plan and run sales discovery calls with questions that uncover pain, budget, and decision process. |
| [`objection-handling`](skills/19-sales-and-customer/objection-handling/SKILL.md) | Prepare responses to common sales objections with empathy and evidence. |
| [`sales-proposal-writer`](skills/19-sales-and-customer/sales-proposal-writer/SKILL.md) | Write persuasive proposals with problem, solution, scope, pricing, and timeline. |
| [`customer-support-replies`](skills/19-sales-and-customer/customer-support-replies/SKILL.md) | Write empathetic, clear customer support replies and macros. |
| [`churn-analysis`](skills/19-sales-and-customer/churn-analysis/SKILL.md) | Analyze why customers leave and design retention actions. |
| [`sales-pipeline-review`](skills/19-sales-and-customer/sales-pipeline-review/SKILL.md) | Review pipeline health: stages, conversion, velocity, and forecast risk. |
| [`negotiation-for-sellers`](skills/19-sales-and-customer/negotiation-for-sellers/SKILL.md) | Prepare commercial negotiations: value anchors, concessions, and trades. |
| [`customer-success-plan`](skills/19-sales-and-customer/customer-success-plan/SKILL.md) | Create customer onboarding and success plans with milestones and health scores. |
| [`faq-and-help-center`](skills/19-sales-and-customer/faq-and-help-center/SKILL.md) | Build FAQs and help center articles that deflect tickets. |
| [`testimonial-and-case-study`](skills/19-sales-and-customer/testimonial-and-case-study/SKILL.md) | Collect testimonials and write case studies with measurable results. |

### Leadership & Management (`skills/20-leadership-and-management/`)

Leading teams, running meetings, and growing people.

| Skill | What it does |
|---|---|
| [`one-on-one-planner`](skills/20-leadership-and-management/one-on-one-planner/SKILL.md) | Plan effective 1:1 meetings with agendas, feedback, and growth topics. |
| [`feedback-giver`](skills/20-leadership-and-management/feedback-giver/SKILL.md) | Give clear, kind, actionable feedback using situation-behavior-impact. |
| [`performance-review-writer`](skills/20-leadership-and-management/performance-review-writer/SKILL.md) | Write fair performance reviews with evidence, ratings, and development plans. |
| [`team-okr-planner`](skills/20-leadership-and-management/team-okr-planner/SKILL.md) | Set team goals and OKRs aligned with company strategy. |
| [`hiring-process-designer`](skills/20-leadership-and-management/hiring-process-designer/SKILL.md) | Design structured hiring processes: scorecards, interview loops, and fair evaluation. |
| [`job-description-writer`](skills/20-leadership-and-management/job-description-writer/SKILL.md) | Write inclusive, clear job descriptions focused on outcomes. |
| [`meeting-facilitation`](skills/20-leadership-and-management/meeting-facilitation/SKILL.md) | Run effective meetings with agendas, timeboxes, decisions, and follow-up. |
| [`delegation-framework`](skills/20-leadership-and-management/delegation-framework/SKILL.md) | Delegate work with clear outcomes, authority, check-ins, and trust. |
| [`conflict-mediation`](skills/20-leadership-and-management/conflict-mediation/SKILL.md) | Mediate workplace disagreements with structured listening and interest-based solutions. |
| [`change-management`](skills/20-leadership-and-management/change-management/SKILL.md) | Plan organizational change: stakeholders, communication, resistance, and rollout. |
| [`strategy-one-pager`](skills/20-leadership-and-management/strategy-one-pager/SKILL.md) | Write a concise strategy: diagnosis, guiding policy, and coherent actions. |
| [`remote-team-practices`](skills/20-leadership-and-management/remote-team-practices/SKILL.md) | Set up healthy remote team habits: async communication, documentation, and rituals. |

### Teaching & Education (`skills/21-teaching-and-education/`)

Lesson design, tutoring, and curriculum for teachers and learners.

| Skill | What it does |
|---|---|
| [`lesson-plan-builder`](skills/21-teaching-and-education/lesson-plan-builder/SKILL.md) | Build lesson plans with objectives, activities, assessment, and differentiation. |
| [`curriculum-designer`](skills/21-teaching-and-education/curriculum-designer/SKILL.md) | Design courses and curricula with sequencing, projects, and assessments. |
| [`quiz-and-exam-writer`](skills/21-teaching-and-education/quiz-and-exam-writer/SKILL.md) | Write quizzes and exams with varied question types, answer keys, and rubrics. |
| [`rubric-builder`](skills/21-teaching-and-education/rubric-builder/SKILL.md) | Create clear grading rubrics with criteria and performance levels. |
| [`explain-by-analogy`](skills/21-teaching-and-education/explain-by-analogy/SKILL.md) | Explain hard ideas using analogies and everyday examples. |
| [`math-tutor`](skills/21-teaching-and-education/math-tutor/SKILL.md) | Tutor math step by step from arithmetic to calculus with hints and checks. |
| [`essay-feedback`](skills/21-teaching-and-education/essay-feedback/SKILL.md) | Give feedback on student essays on thesis, evidence, structure, and style. |
| [`active-learning-activities`](skills/21-teaching-and-education/active-learning-activities/SKILL.md) | Design active learning activities like think-pair-share, jigsaws, and case studies. |
| [`homeschool-planner`](skills/21-teaching-and-education/homeschool-planner/SKILL.md) | Plan homeschool schedules, subjects, and resources by age. |
| [`workshop-designer`](skills/21-teaching-and-education/workshop-designer/SKILL.md) | Design workshops and training sessions with exercises, timing, and materials. |
| [`study-skills-coach`](skills/21-teaching-and-education/study-skills-coach/SKILL.md) | Teach study techniques: retrieval practice, spacing, note-taking, and focus. |
| [`presentation-teacher`](skills/21-teaching-and-education/presentation-teacher/SKILL.md) | Teach and review presentation skills: structure, slides, delivery, and Q&A. |

### Music & Audio (`skills/22-music-and-audio/`)

Composition, production, theory, and sound design.

| Skill | What it does |
|---|---|
| [`music-theory-coach`](skills/22-music-and-audio/music-theory-coach/SKILL.md) | Explain music theory: scales, chords, keys, intervals, and progressions. |
| [`chord-progression-writer`](skills/22-music-and-audio/chord-progression-writer/SKILL.md) | Create chord progressions in styles and keys with voicing and rhythm ideas. |
| [`songwriting-coach`](skills/22-music-and-audio/songwriting-coach/SKILL.md) | Coach songwriting: structure, hooks, melody, and lyrics. |
| [`mixing-and-mastering`](skills/22-music-and-audio/mixing-and-mastering/SKILL.md) | Guide mixing and mastering: EQ, compression, levels, panning, and loudness. |
| [`sound-design-synthesis`](skills/22-music-and-audio/sound-design-synthesis/SKILL.md) | Design sounds with synthesis: oscillators, filters, envelopes, and modulation. |
| [`beat-making`](skills/22-music-and-audio/beat-making/SKILL.md) | Build drum patterns and beats across genres. |
| [`instrument-practice-plan`](skills/22-music-and-audio/instrument-practice-plan/SKILL.md) | Plan structured practice for guitar, piano, drums, or voice. |
| [`game-audio-design`](skills/22-music-and-audio/game-audio-design/SKILL.md) | Design game audio: music layers, SFX, mixing, and implementation in engines. |
| [`podcast-producer`](skills/22-music-and-audio/podcast-producer/SKILL.md) | Plan and produce podcasts: format, episodes, recording, editing, and publishing. |
| [`dj-set-planner`](skills/22-music-and-audio/dj-set-planner/SKILL.md) | Plan DJ sets with energy curves, harmonic mixing, and transitions. |

### Video, Photo & Media (`skills/23-video-photo-media/`)

Filmmaking, editing, and photography.

| Skill | What it does |
|---|---|
| [`video-script-writer`](skills/23-video-photo-media/video-script-writer/SKILL.md) | Write scripts for videos with hooks, structure, and visual cues. |
| [`storyboard-builder`](skills/23-video-photo-media/storyboard-builder/SKILL.md) | Create storyboards and shot lists for videos and animations. |
| [`video-editing-workflow`](skills/23-video-photo-media/video-editing-workflow/SKILL.md) | Organize editing: ingest, rough cut, pacing, color, audio, and export. |
| [`photography-composition`](skills/23-video-photo-media/photography-composition/SKILL.md) | Teach composition: rule of thirds, leading lines, light, and framing. |
| [`camera-settings-guide`](skills/23-video-photo-media/camera-settings-guide/SKILL.md) | Explain exposure: aperture, shutter, ISO, and modes for situations. |
| [`photo-editing-workflow`](skills/23-video-photo-media/photo-editing-workflow/SKILL.md) | Edit photos in Lightroom or Photoshop: culling, tone, color, and export. |
| [`thumbnail-designer`](skills/23-video-photo-media/thumbnail-designer/SKILL.md) | Design click-worthy thumbnails with strong focal points and text. |
| [`short-film-planner`](skills/23-video-photo-media/short-film-planner/SKILL.md) | Plan short films: concept, script, crew, schedule, and budget. |
| [`livestream-setup`](skills/23-video-photo-media/livestream-setup/SKILL.md) | Set up livestreams: OBS scenes, audio, overlays, and chat tools. |
| [`subtitle-and-captions`](skills/23-video-photo-media/subtitle-and-captions/SKILL.md) | Create accurate captions and subtitles with timing and style rules. |
| [`brand-photography-brief`](skills/23-video-photo-media/brand-photography-brief/SKILL.md) | Write briefs for product or brand photoshoots with shot lists and style. |
| [`image-prompt-writer`](skills/23-video-photo-media/image-prompt-writer/SKILL.md) | Write effective prompts for AI image generators with subject, style, lighting, and composition. |

### 3D, Art & Animation (`skills/24-3d-art-and-animation/`)

Modeling, shaders, animation, and visual art.

| Skill | What it does |
|---|---|
| [`blender-modeling`](skills/24-3d-art-and-animation/blender-modeling/SKILL.md) | Guide 3D modeling in Blender: topology, modifiers, UVs, and materials. |
| [`character-rigging`](skills/24-3d-art-and-animation/character-rigging/SKILL.md) | Rig characters with bones, weights, IK, and controls. |
| [`animation-principles`](skills/24-3d-art-and-animation/animation-principles/SKILL.md) | Apply the 12 principles of animation: timing, squash, anticipation, and arcs. |
| [`shader-writing`](skills/24-3d-art-and-animation/shader-writing/SKILL.md) | Write shaders in GLSL, HLSL, or Godot shading language: lighting, effects, and optimization. |
| [`texture-and-materials`](skills/24-3d-art-and-animation/texture-and-materials/SKILL.md) | Create PBR materials: albedo, roughness, metallic, and normal maps. |
| [`low-poly-art-style`](skills/24-3d-art-and-animation/low-poly-art-style/SKILL.md) | Define and produce low-poly art: palettes, flat shading, and optimization. |
| [`environment-art`](skills/24-3d-art-and-animation/environment-art/SKILL.md) | Build game environments: blockout, modularity, lighting, and atmosphere. |
| [`vfx-particles`](skills/24-3d-art-and-animation/vfx-particles/SKILL.md) | Design particle effects for fire, smoke, magic, and impacts. |
| [`concept-art-brief`](skills/24-3d-art-and-animation/concept-art-brief/SKILL.md) | Write concept art briefs and critique for characters, creatures, and environments. |
| [`sprite-animation`](skills/24-3d-art-and-animation/sprite-animation/SKILL.md) | Plan 2D sprite animation: frame counts, timing, spritesheets, and engine import. |

### Making & Hobbies (`skills/25-making-and-hobbies/`)

Electronics, 3D printing, woodworking, cooking, gardening and other hands-on projects.

| Skill | What it does |
|---|---|
| [`arduino-esp32`](skills/25-making-and-hobbies/arduino-esp32/SKILL.md) | Build Arduino and ESP32 projects: sensors, actuators, wiring, and firmware. |
| [`raspberry-pi-projects`](skills/25-making-and-hobbies/raspberry-pi-projects/SKILL.md) | Plan Raspberry Pi projects: setup, GPIO, services, and headless operation. |
| [`3d-printing-guide`](skills/25-making-and-hobbies/3d-printing-guide/SKILL.md) | Troubleshoot and plan 3D prints: slicer settings, materials, supports, and calibration. |
| [`cad-design-basics`](skills/25-making-and-hobbies/cad-design-basics/SKILL.md) | Design parts in CAD (Fusion, FreeCAD, Onshape) with sketches, constraints, and tolerances. |
| [`woodworking-planner`](skills/25-making-and-hobbies/woodworking-planner/SKILL.md) | Plan woodworking projects: cut lists, joinery, finishes, and tool needs. |
| [`diy-electronics-repair`](skills/25-making-and-hobbies/diy-electronics-repair/SKILL.md) | Diagnose and repair common household electronics at the component and connector level using safe low-voltage practices. |
| [`cooking-recipe-developer`](skills/25-making-and-hobbies/cooking-recipe-developer/SKILL.md) | Develop and adapt recipes with techniques, substitutions, scaling, and timing. |
| [`coffee-brewing`](skills/25-making-and-hobbies/coffee-brewing/SKILL.md) | Dial in coffee brewing: grind, ratio, temperature, and method. |
| [`gardening-planner`](skills/25-making-and-hobbies/gardening-planner/SKILL.md) | Plan gardens with layout, planting calendar, soil, and companion planting. |
| [`bike-maintenance`](skills/25-making-and-hobbies/bike-maintenance/SKILL.md) | Maintain bicycles: drivetrain, brakes, tires, and tune-ups. |
| [`car-maintenance-basics`](skills/25-making-and-hobbies/car-maintenance-basics/SKILL.md) | Explain routine car maintenance: fluids, tires, filters, and diagnostic codes. |
| [`camping-trip-planner`](skills/25-making-and-hobbies/camping-trip-planner/SKILL.md) | Plan camping and hiking trips: route, gear, food, and contingencies. |
| [`board-game-designer`](skills/25-making-and-hobbies/board-game-designer/SKILL.md) | Design tabletop games: mechanics, components, balance, and playtesting. |
| [`ttrpg-campaign-builder`](skills/25-making-and-hobbies/ttrpg-campaign-builder/SKILL.md) | Build tabletop RPG campaigns and sessions with hooks, NPCs, encounters, and maps. |
| [`knitting-and-sewing`](skills/25-making-and-hobbies/knitting-and-sewing/SKILL.md) | Plan sewing and knitting projects: patterns, measurements, fabrics, and techniques. |
| [`home-automation`](skills/25-making-and-hobbies/home-automation/SKILL.md) | Set up smart home automation with Home Assistant, sensors, and routines. |

### Security & Privacy (`skills/26-security-and-privacy/`)

Defensive security, privacy hygiene, and safe engineering.

| Skill | What it does |
|---|---|
| [`threat-modeling`](skills/26-security-and-privacy/threat-modeling/SKILL.md) | Threat model systems with STRIDE: assets, trust boundaries, threats, and mitigations. |
| [`owasp-checklist`](skills/26-security-and-privacy/owasp-checklist/SKILL.md) | Review web apps against the OWASP Top 10 with fixes. |
| [`password-and-account-hygiene`](skills/26-security-and-privacy/password-and-account-hygiene/SKILL.md) | Advise on password managers, MFA, passkeys, and recovery planning. |
| [`privacy-policy-drafter`](skills/26-security-and-privacy/privacy-policy-drafter/SKILL.md) | Draft plain-language privacy policies and data inventories for apps. |
| [`secure-code-checklist`](skills/26-security-and-privacy/secure-code-checklist/SKILL.md) | Apply secure coding practices: validation, encoding, least privilege, and dependency hygiene. |
| [`dependency-vulnerability-triage`](skills/26-security-and-privacy/dependency-vulnerability-triage/SKILL.md) | Triage dependency vulnerabilities from audit tools by reachability and severity. |
| [`home-network-security`](skills/26-security-and-privacy/home-network-security/SKILL.md) | Secure a home network: router settings, segmentation, DNS, and updates. |
| [`api-security-review`](skills/26-security-and-privacy/api-security-review/SKILL.md) | Review APIs for authentication, authorization, rate limits, and data exposure. |
| [`incident-readiness-plan`](skills/26-security-and-privacy/incident-readiness-plan/SKILL.md) | Prepare a small team's security incident plan: roles, contacts, and steps. |
| [`data-privacy-compliance-overview`](skills/26-security-and-privacy/data-privacy-compliance-overview/SKILL.md) | Explain GDPR/CCPA concepts: lawful basis, consent, access requests, and retention. |
| [`ctf-and-learning-labs`](skills/26-security-and-privacy/ctf-and-learning-labs/SKILL.md) | Guide learning cybersecurity ethically through legal labs, CTFs, and courses. |
| [`encryption-basics`](skills/26-security-and-privacy/encryption-basics/SKILL.md) | Explain encryption, hashing, TLS, and key management at a practical level. |

### Automation & No-Code (`skills/27-automation-and-no-code/`)

Automating work with scripts, workflows, and no-code tools.

| Skill | What it does |
|---|---|
| [`workflow-automation-designer`](skills/27-automation-and-no-code/workflow-automation-designer/SKILL.md) | Design automations with triggers, steps, error handling, and monitoring across tools. |
| [`n8n-make-zapier`](skills/27-automation-and-no-code/n8n-make-zapier/SKILL.md) | Build workflows in n8n, Make, and Zapier with webhooks, filters, and data mapping. |
| [`google-apps-script`](skills/27-automation-and-no-code/google-apps-script/SKILL.md) | Automate Google Sheets, Docs, and Gmail with Apps Script. |
| [`excel-formulas`](skills/27-automation-and-no-code/excel-formulas/SKILL.md) | Write and debug Excel and Google Sheets formulas: lookups, arrays, dates, and text. |
| [`spreadsheet-modeling`](skills/27-automation-and-no-code/spreadsheet-modeling/SKILL.md) | Design clean spreadsheet models with inputs, calculations, and outputs separated. |
| [`airtable-notion-databases`](skills/27-automation-and-no-code/airtable-notion-databases/SKILL.md) | Design databases in Notion or Airtable: tables, relations, views, and automations. |
| [`obsidian-note-system`](skills/27-automation-and-no-code/obsidian-note-system/SKILL.md) | Build a note-taking system in Obsidian or similar: linking, templates, and review. |
| [`python-automation-scripts`](skills/27-automation-and-no-code/python-automation-scripts/SKILL.md) | Write Python scripts to automate files, APIs, spreadsheets, and email. |
| [`api-integration-planner`](skills/27-automation-and-no-code/api-integration-planner/SKILL.md) | Plan integrations between APIs: auth, rate limits, mapping, and retries. |
| [`email-automation-rules`](skills/27-automation-and-no-code/email-automation-rules/SKILL.md) | Create email filters, templates, and routing rules to reduce inbox load. |
| [`browser-automation`](skills/27-automation-and-no-code/browser-automation/SKILL.md) | Automate browsers with Playwright or Puppeteer: testing, forms, and scraping within site terms. |
| [`personal-dashboard-builder`](skills/27-automation-and-no-code/personal-dashboard-builder/SKILL.md) | Build a personal dashboard aggregating tasks, calendar, and metrics. |

### Product & Startup (`skills/28-product-and-startup/`)

Product management, strategy, and early-stage building.

| Skill | What it does |
|---|---|
| [`prd-writer`](skills/28-product-and-startup/prd-writer/SKILL.md) | Write product requirement documents with problem, users, goals, scope, and acceptance criteria. |
| [`user-story-writer`](skills/28-product-and-startup/user-story-writer/SKILL.md) | Write user stories with acceptance criteria and edge cases. |
| [`roadmap-planner`](skills/28-product-and-startup/roadmap-planner/SKILL.md) | Build product roadmaps with themes, outcomes, and now/next/later horizons. |
| [`feature-prioritization`](skills/28-product-and-startup/feature-prioritization/SKILL.md) | Prioritize features with RICE, MoSCoW, or Kano. |
| [`mvp-scoping`](skills/28-product-and-startup/mvp-scoping/SKILL.md) | Scope a minimum viable product to test the riskiest assumption fast. |
| [`product-metrics`](skills/28-product-and-startup/product-metrics/SKILL.md) | Define product metrics: activation, retention, engagement, and north star. |
| [`pitch-deck-builder`](skills/28-product-and-startup/pitch-deck-builder/SKILL.md) | Build investor pitch decks: problem, solution, market, traction, team, and ask. |
| [`startup-idea-generator`](skills/28-product-and-startup/startup-idea-generator/SKILL.md) | Generate startup ideas from problems, trends, and personal skills. |
| [`okr-for-startups`](skills/28-product-and-startup/okr-for-startups/SKILL.md) | Set lightweight OKRs for early-stage teams. |
| [`competitive-teardown`](skills/28-product-and-startup/competitive-teardown/SKILL.md) | Tear down competitor products: features, UX, pricing, and weaknesses. |
| [`launch-checklist`](skills/28-product-and-startup/launch-checklist/SKILL.md) | Run a pre-launch checklist: QA, analytics, legal pages, support, and rollback. |
| [`saas-pricing-tiers`](skills/28-product-and-startup/saas-pricing-tiers/SKILL.md) | Design SaaS pricing tiers, limits, and upgrade triggers. |
| [`retention-playbook`](skills/28-product-and-startup/retention-playbook/SKILL.md) | Build retention playbooks: onboarding, habit loops, reminders, and win-back. |
| [`user-research-synthesis`](skills/28-product-and-startup/user-research-synthesis/SKILL.md) | Synthesize interviews and feedback into themes and decisions. |

### Game Dev: Engines & Systems (`skills/29-gamedev-engines-and-systems/`)

Godot, Unity, Unreal, and reusable gameplay systems.

| Skill | What it does |
|---|---|
| [`godot-multiplayer`](skills/29-gamedev-engines-and-systems/godot-multiplayer/SKILL.md) | Build Godot 4 multiplayer: ENet, authority, spawners, synchronizers, RPCs, lobbies, and prediction. |
| [`godot-ui-themes`](skills/29-gamedev-engines-and-systems/godot-ui-themes/SKILL.md) | Build Godot 4 UI with Control nodes, containers, themes, and responsive layouts. |
| [`godot-3d-character`](skills/29-gamedev-engines-and-systems/godot-3d-character/SKILL.md) | Create Godot 4 3D character controllers: movement, camera, jumping, slopes, animation trees. |
| [`godot-2d-platformer`](skills/29-gamedev-engines-and-systems/godot-2d-platformer/SKILL.md) | Build Godot 4 2D platformers: movement feel, coyote time, buffering, tilemaps, and enemies. |
| [`godot-save-load`](skills/29-gamedev-engines-and-systems/godot-save-load/SKILL.md) | Implement Godot save and load systems with JSON, resources, versioning, and autosave. |
| [`godot-ai-navigation`](skills/29-gamedev-engines-and-systems/godot-ai-navigation/SKILL.md) | Add Godot enemy AI: state machines, NavigationAgent, perception, and behavior trees. |
| [`godot-export-and-release`](skills/29-gamedev-engines-and-systems/godot-export-and-release/SKILL.md) | Export and publish Godot games to desktop, web, and mobile with presets and optimization. |
| [`godot-performance`](skills/29-gamedev-engines-and-systems/godot-performance/SKILL.md) | Optimize Godot games: profiling, draw calls, physics, pooling, and GDScript tuning. |
| [`unity-csharp`](skills/29-gamedev-engines-and-systems/unity-csharp/SKILL.md) | Write Unity C# with MonoBehaviours, ScriptableObjects, coroutines, and the new Input System. |
| [`unreal-blueprints-cpp`](skills/29-gamedev-engines-and-systems/unreal-blueprints-cpp/SKILL.md) | Work in Unreal with Blueprints and C++: gameplay framework, replication, and performance. |
| [`game-state-machines`](skills/29-gamedev-engines-and-systems/game-state-machines/SKILL.md) | Implement finite and hierarchical state machines for players, enemies, and game flow. |
| [`inventory-and-items`](skills/29-gamedev-engines-and-systems/inventory-and-items/SKILL.md) | Design inventory, items, equipment, and crafting systems with data-driven definitions. |
| [`combat-system-design`](skills/29-gamedev-engines-and-systems/combat-system-design/SKILL.md) | Design melee, ranged, and ability combat: hitboxes, cooldowns, damage models, and feedback. |
| [`game-camera-systems`](skills/29-gamedev-engines-and-systems/game-camera-systems/SKILL.md) | Create game cameras: follow, look-ahead, shake, cinematic, and split-screen. |
| [`emulator-frontend-ui`](skills/29-gamedev-engines-and-systems/emulator-frontend-ui/SKILL.md) | Design emulator or game-launcher frontends: library views, controller navigation, artwork, and settings, for legally obtained software. |
| [`game-jam-playbook`](skills/29-gamedev-engines-and-systems/game-jam-playbook/SKILL.md) | Plan and finish game jams: scope, schedule, theme interpretation, and submission. |
| [`game-monetization-ethics`](skills/29-gamedev-engines-and-systems/game-monetization-ethics/SKILL.md) | Plan fair game monetization: premium, DLC, ads, and cosmetic items without dark patterns. |
| [`steam-page-and-launch`](skills/29-gamedev-engines-and-systems/steam-page-and-launch/SKILL.md) | Prepare a Steam or itch.io page: capsule art, trailer, description, wishlists, and launch timing. |

### Mobile Apps (`skills/30-mobile-apps/`)

iOS, Android, and cross-platform app development.

| Skill | What it does |
|---|---|
| [`swiftui-views`](skills/30-mobile-apps/swiftui-views/SKILL.md) | Build iOS UIs with SwiftUI: layout, state, navigation, lists, and animations. |
| [`kotlin-android`](skills/30-mobile-apps/kotlin-android/SKILL.md) | Build Android apps with Kotlin and Jetpack Compose: state, navigation, Room, and coroutines. |
| [`flutter-dart`](skills/30-mobile-apps/flutter-dart/SKILL.md) | Build cross-platform apps with Flutter: widgets, state, navigation, and platform channels. |
| [`react-native`](skills/30-mobile-apps/react-native/SKILL.md) | Build apps with React Native and Expo: navigation, native modules, and performance. |
| [`app-store-release`](skills/30-mobile-apps/app-store-release/SKILL.md) | Publish apps on the App Store and Google Play: listings, review guidelines, signing, and updates. |
| [`mobile-ux-patterns`](skills/30-mobile-apps/mobile-ux-patterns/SKILL.md) | Apply mobile UX patterns: navigation, gestures, thumb zones, and offline behavior. |
| [`offline-first-sync`](skills/30-mobile-apps/offline-first-sync/SKILL.md) | Design offline-first apps with local storage, sync queues, and conflict resolution. |
| [`push-notifications`](skills/30-mobile-apps/push-notifications/SKILL.md) | Implement push notifications with APNs and FCM, permissions, and relevance. |
| [`mobile-performance`](skills/30-mobile-apps/mobile-performance/SKILL.md) | Optimize mobile apps: startup time, memory, battery, and scrolling smoothness. |
| [`in-app-purchases`](skills/30-mobile-apps/in-app-purchases/SKILL.md) | Implement in-app purchases and subscriptions with StoreKit and Play Billing. |

### AI & LLM Engineering (`skills/31-ai-and-llm-engineering/`)

Building products with language models: prompts, RAG, agents, and evals.

| Skill | What it does |
|---|---|
| [`rag-system-design`](skills/31-ai-and-llm-engineering/rag-system-design/SKILL.md) | Design retrieval-augmented generation: chunking, embeddings, vector stores, reranking, and evaluation. |
| [`llm-evals`](skills/31-ai-and-llm-engineering/llm-evals/SKILL.md) | Build evaluation suites for LLM apps: test sets, graders, regressions, and metrics. |
| [`tool-use-and-function-calling`](skills/31-ai-and-llm-engineering/tool-use-and-function-calling/SKILL.md) | Design tools for LLM function calling: schemas, descriptions, error handling, and safety. |
| [`prompt-patterns`](skills/31-ai-and-llm-engineering/prompt-patterns/SKILL.md) | Apply prompting patterns: few-shot, chain of thought, structured output, and role setup. |
| [`structured-output-json`](skills/31-ai-and-llm-engineering/structured-output-json/SKILL.md) | Get reliable JSON from LLMs with schemas, validation, and repair loops. |
| [`ai-agent-architecture`](skills/31-ai-and-llm-engineering/ai-agent-architecture/SKILL.md) | Architect AI agents: planning loops, memory, tool routing, and guardrails. |
| [`embeddings-and-search`](skills/31-ai-and-llm-engineering/embeddings-and-search/SKILL.md) | Build semantic search with embeddings, hybrid retrieval, and metadata filters. |
| [`llm-cost-and-latency`](skills/31-ai-and-llm-engineering/llm-cost-and-latency/SKILL.md) | Reduce LLM cost and latency with caching, smaller models, batching, and prompt trimming. |
| [`ai-safety-guardrails`](skills/31-ai-and-llm-engineering/ai-safety-guardrails/SKILL.md) | Add guardrails to AI apps: input filtering, output checks, prompt-injection defense, and logging. |
| [`fine-tuning-guide`](skills/31-ai-and-llm-engineering/fine-tuning-guide/SKILL.md) | Decide whether and how to fine-tune models: data prep, methods, and evaluation. |
| [`chatbot-conversation-design`](skills/31-ai-and-llm-engineering/chatbot-conversation-design/SKILL.md) | Design chatbot conversations: persona, flows, fallbacks, and handoff. |
| [`claude-api-integration`](skills/31-ai-and-llm-engineering/claude-api-integration/SKILL.md) | Integrate the Claude API: messages, system prompts, tools, streaming, and error handling. |
| [`voice-assistant-design`](skills/31-ai-and-llm-engineering/voice-assistant-design/SKILL.md) | Design voice interfaces: wake words, turn-taking, speech recognition, and TTS. |
| [`ai-product-ideas`](skills/31-ai-and-llm-engineering/ai-product-ideas/SKILL.md) | Brainstorm AI product ideas from workflows with repetitive judgment or text work. |
| [`dataset-curation`](skills/31-ai-and-llm-engineering/dataset-curation/SKILL.md) | Curate and label datasets for ML and evals: sourcing, quality, bias, and licensing. |
| [`multi-agent-workflows`](skills/31-ai-and-llm-engineering/multi-agent-workflows/SKILL.md) | Design multi-agent systems with roles, handoffs, and shared state. |

### Creative Writing (`skills/32-creative-writing/`)

Fiction, poetry, screenwriting, and story craft.

| Skill | What it does |
|---|---|
| [`novel-outliner`](skills/32-creative-writing/novel-outliner/SKILL.md) | Outline novels with premise, acts, character arcs, and chapter beats. |
| [`short-story-workshop`](skills/32-creative-writing/short-story-workshop/SKILL.md) | Draft and revise short stories: hook, conflict, turn, and ending. |
| [`screenplay-formatter`](skills/32-creative-writing/screenplay-formatter/SKILL.md) | Write and format screenplays with scenes, action lines, and dialogue. |
| [`poetry-craft`](skills/32-creative-writing/poetry-craft/SKILL.md) | Write original poems with imagery, rhythm, and form guidance, from free verse to sonnets. |
| [`plot-hole-finder`](skills/32-creative-writing/plot-hole-finder/SKILL.md) | Find plot holes and continuity errors in stories. |
| [`fantasy-magic-system`](skills/32-creative-writing/fantasy-magic-system/SKILL.md) | Design magic systems with rules, costs, limits, and consequences. |
| [`villain-and-conflict`](skills/32-creative-writing/villain-and-conflict/SKILL.md) | Create compelling antagonists and conflicts with believable motives. |
| [`dialogue-polish`](skills/32-creative-writing/dialogue-polish/SKILL.md) | Polish dialogue: voice, subtext, rhythm, and tags. |
| [`writing-prompts-and-sprints`](skills/32-creative-writing/writing-prompts-and-sprints/SKILL.md) | Generate writing prompts and run timed sprints to beat blocks. |
| [`fanfiction-and-roleplay-scenes`](skills/32-creative-writing/fanfiction-and-roleplay-scenes/SKILL.md) | Write original scenes and collaborative roleplay with consistent characters and tone. |
| [`story-structure-analyzer`](skills/32-creative-writing/story-structure-analyzer/SKILL.md) | Analyze story structure using three-act, save-the-cat, and hero's journey. |
| [`interactive-fiction-design`](skills/32-creative-writing/interactive-fiction-design/SKILL.md) | Design branching narrative and interactive fiction with Ink, Twine, or Yarn. |

### Communication & Social (`skills/33-communication-and-social/`)

Speaking, difficult conversations, networking, and everyday communication.

| Skill | What it does |
|---|---|
| [`public-speaking-coach`](skills/33-communication-and-social/public-speaking-coach/SKILL.md) | Coach public speaking: structure, openings, delivery, and nerves-friendly rehearsal. |
| [`difficult-conversation-prep`](skills/33-communication-and-social/difficult-conversation-prep/SKILL.md) | Prepare for hard conversations with outcomes, framing, and scripts. |
| [`networking-coach`](skills/33-communication-and-social/networking-coach/SKILL.md) | Build professional networks with outreach, follow-ups, and value-first habits. |
| [`apology-and-repair`](skills/33-communication-and-social/apology-and-repair/SKILL.md) | Write sincere apologies and repair plans. |
| [`persuasive-argument`](skills/33-communication-and-social/persuasive-argument/SKILL.md) | Build persuasive arguments with claims, evidence, and counterpoints ethically. |
| [`toast-and-speech-writer`](skills/33-communication-and-social/toast-and-speech-writer/SKILL.md) | Write toasts, eulogies-adjacent tributes, and speeches for weddings and events. |
| [`linkedin-profile`](skills/33-communication-and-social/linkedin-profile/SKILL.md) | Write and optimize professional profiles and posts. |
| [`cover-letter-writer`](skills/33-communication-and-social/cover-letter-writer/SKILL.md) | Write tailored cover letters and application messages. |
| [`resume-builder`](skills/33-communication-and-social/resume-builder/SKILL.md) | Build and tighten resumes with impact bullets and clean structure. |
| [`small-talk-and-rapport`](skills/33-communication-and-social/small-talk-and-rapport/SKILL.md) | Practice conversation skills: questions, listening, and keeping dialogue flowing. |
| [`text-message-reply`](skills/33-communication-and-social/text-message-reply/SKILL.md) | Draft thoughtful replies to texts and messages with the right tone. |
| [`event-planner`](skills/33-communication-and-social/event-planner/SKILL.md) | Plan parties and events: budget, timeline, vendors, and run-of-show. |

### Math & Science (`skills/34-math-and-science/`)

Quantitative reasoning, physics, chemistry basics, and problem solving.

| Skill | What it does |
|---|---|
| [`math-problem-solver`](skills/34-math-and-science/math-problem-solver/SKILL.md) | Solve math problems step by step across algebra, geometry, calculus, and discrete math. |
| [`proof-writing`](skills/34-math-and-science/proof-writing/SKILL.md) | Write and check mathematical proofs: direct, contradiction, induction. |
| [`physics-problem-solver`](skills/34-math-and-science/physics-problem-solver/SKILL.md) | Solve physics problems with diagrams, knowns, equations, units, and sanity checks. |
| [`unit-conversion-and-estimation`](skills/34-math-and-science/unit-conversion-and-estimation/SKILL.md) | Convert units and do Fermi estimates with clear assumptions. |
| [`probability-puzzles`](skills/34-math-and-science/probability-puzzles/SKILL.md) | Solve probability problems with counting, conditional probability, and Bayes. |
| [`linear-algebra-intuition`](skills/34-math-and-science/linear-algebra-intuition/SKILL.md) | Explain linear algebra with geometric intuition: vectors, matrices, eigenvalues. |
| [`calculus-coach`](skills/34-math-and-science/calculus-coach/SKILL.md) | Teach calculus: limits, derivatives, integrals, and applications. |
| [`chemistry-concepts`](skills/34-math-and-science/chemistry-concepts/SKILL.md) | Explain chemistry concepts: atoms, bonding, reactions, stoichiometry. |
| [`scientific-method-helper`](skills/34-math-and-science/scientific-method-helper/SKILL.md) | Design experiments and reason about evidence: hypotheses, controls, and confounds. |
| [`science-fair-project`](skills/34-math-and-science/science-fair-project/SKILL.md) | Plan science fair projects from idea to presentation. |
| [`astronomy-basics`](skills/34-math-and-science/astronomy-basics/SKILL.md) | Explain astronomy and space concepts, stargazing basics, and orbital mechanics. |
| [`engineering-estimation`](skills/34-math-and-science/engineering-estimation/SKILL.md) | Do back-of-the-envelope engineering calculations: loads, power, flow, and tolerances. |

### Office & Documents (`skills/35-office-and-documents/`)

Slides, reports, templates, and everyday office work.

| Skill | What it does |
|---|---|
| [`slide-deck-structure`](skills/35-office-and-documents/slide-deck-structure/SKILL.md) | Structure presentation decks with story, one idea per slide, and clean visuals. |
| [`report-writer`](skills/35-office-and-documents/report-writer/SKILL.md) | Write business and technical reports with executive summary, findings, and recommendations. |
| [`sop-writer`](skills/35-office-and-documents/sop-writer/SKILL.md) | Write standard operating procedures with clear steps, roles, and checks. |
| [`checklist-builder`](skills/35-office-and-documents/checklist-builder/SKILL.md) | Create effective checklists for recurring tasks and launches. |
| [`contract-plain-english`](skills/35-office-and-documents/contract-plain-english/SKILL.md) | Summarize contracts in plain English and flag unusual clauses to ask a lawyer about. |
| [`document-template-maker`](skills/35-office-and-documents/document-template-maker/SKILL.md) | Create reusable templates for proposals, invoices, briefs, and notes. |
| [`meeting-agenda-builder`](skills/35-office-and-documents/meeting-agenda-builder/SKILL.md) | Build agendas with goals, timeboxes, and pre-reads. |
| [`project-status-report`](skills/35-office-and-documents/project-status-report/SKILL.md) | Write concise status reports: progress, risks, decisions, and next steps. |
| [`faq-document-builder`](skills/35-office-and-documents/faq-document-builder/SKILL.md) | Compile FAQs from questions and answers with clear structure. |
| [`knowledge-base-organizer`](skills/35-office-and-documents/knowledge-base-organizer/SKILL.md) | Organize team knowledge bases: taxonomy, naming, ownership, and cleanup. |
| [`translation-and-localization`](skills/35-office-and-documents/translation-and-localization/SKILL.md) | Translate and localize text with tone, idioms, and cultural adaptation. |
| [`data-entry-cleanup`](skills/35-office-and-documents/data-entry-cleanup/SKILL.md) | Standardize and clean lists, names, addresses, and records for import. |

### E-commerce & Retail (`skills/36-ecommerce-and-retail/`)

Selling products online: listings, operations, ads, and marketplaces.

| Skill | What it does |
|---|---|
| [`product-listing-writer`](skills/36-ecommerce-and-retail/product-listing-writer/SKILL.md) | Write product titles, bullets, and descriptions that rank and convert on Shopify, Etsy, Amazon, and eBay. |
| [`ecommerce-store-setup`](skills/36-ecommerce-and-retail/ecommerce-store-setup/SKILL.md) | Plan an online store: platform choice, catalog, payments, shipping, taxes, and policies. |
| [`dropship-vs-inventory`](skills/36-ecommerce-and-retail/dropship-vs-inventory/SKILL.md) | Compare dropshipping, print-on-demand, wholesale, and making your own products. |
| [`marketplace-fee-calculator`](skills/36-ecommerce-and-retail/marketplace-fee-calculator/SKILL.md) | Calculate net profit after marketplace fees, shipping, and returns across eBay, Etsy, Amazon, and others. |
| [`shipping-and-fulfillment`](skills/36-ecommerce-and-retail/shipping-and-fulfillment/SKILL.md) | Plan shipping: carriers, packaging, rates, labels, and returns. |
| [`product-photography-setup`](skills/36-ecommerce-and-retail/product-photography-setup/SKILL.md) | Set up DIY product photography with lighting, backdrops, angles, and editing. |
| [`cart-abandonment-recovery`](skills/36-ecommerce-and-retail/cart-abandonment-recovery/SKILL.md) | Reduce cart abandonment with checkout fixes and recovery emails. |
| [`inventory-forecasting`](skills/36-ecommerce-and-retail/inventory-forecasting/SKILL.md) | Forecast stock needs from sales velocity, lead times, and seasonality. |
| [`etsy-seo`](skills/36-ecommerce-and-retail/etsy-seo/SKILL.md) | Optimize Etsy shops: tags, titles, categories, and photos for search. |
| [`thrift-and-flip-sourcing`](skills/36-ecommerce-and-retail/thrift-and-flip-sourcing/SKILL.md) | Source resale inventory from thrift stores, estate sales, and auctions with margin math. |
| [`subscription-box-planner`](skills/36-ecommerce-and-retail/subscription-box-planner/SKILL.md) | Plan a subscription box business: curation, costs, churn, and logistics. |
| [`print-on-demand-design`](skills/36-ecommerce-and-retail/print-on-demand-design/SKILL.md) | Create print-on-demand designs and mockups with niche research. |
| [`customer-returns-policy`](skills/36-ecommerce-and-retail/customer-returns-policy/SKILL.md) | Write fair returns, refunds, and warranty policies. |

### Real Estate & Property (`skills/37-real-estate-and-property/`)

Renting, buying, and managing property (educational).

| Skill | What it does |
|---|---|
| [`rental-property-analysis`](skills/37-real-estate-and-property/rental-property-analysis/SKILL.md) | Analyze rental properties: cash flow, cap rate, cash-on-cash return, and expenses. |
| [`home-buying-checklist`](skills/37-real-estate-and-property/home-buying-checklist/SKILL.md) | Guide first-time home buying: budget, mortgage prep, inspection, and closing. |
| [`tenant-screening-process`](skills/37-real-estate-and-property/tenant-screening-process/SKILL.md) | Design a fair tenant screening process with consistent criteria. |
| [`lease-reader`](skills/37-real-estate-and-property/lease-reader/SKILL.md) | Explain residential lease terms in plain English and flag questions to ask. |
| [`moving-planner`](skills/37-real-estate-and-property/moving-planner/SKILL.md) | Plan a move: timeline, budget, packing, and address changes. |
| [`home-renovation-budget`](skills/37-real-estate-and-property/home-renovation-budget/SKILL.md) | Budget renovation projects with scope, contingency, and contractor comparison. |
| [`airbnb-host-playbook`](skills/37-real-estate-and-property/airbnb-host-playbook/SKILL.md) | Run a short-term rental: listing, pricing, cleaning, reviews, and rules. |
| [`neighborhood-research`](skills/37-real-estate-and-property/neighborhood-research/SKILL.md) | Research neighborhoods: commute, amenities, costs, and trade-offs. |

### Open Source & Community (`skills/38-open-source-and-community/`)

Starting, maintaining, and growing open-source projects.

| Skill | What it does |
|---|---|
| [`open-source-launch`](skills/38-open-source-and-community/open-source-launch/SKILL.md) | Launch an open-source project: license, README, contributing guide, issues, and first release. |
| [`license-chooser`](skills/38-open-source-and-community/license-chooser/SKILL.md) | Choose an open-source license: MIT, Apache, GPL, and implications. |
| [`issue-triage`](skills/38-open-source-and-community/issue-triage/SKILL.md) | Triage GitHub issues: labels, reproduction, priority, and closing. |
| [`pull-request-review-guide`](skills/38-open-source-and-community/pull-request-review-guide/SKILL.md) | Review contributor pull requests constructively with checklists. |
| [`changelog-and-releases`](skills/38-open-source-and-community/changelog-and-releases/SKILL.md) | Write changelogs and release notes with semantic versioning. |
| [`code-of-conduct-and-governance`](skills/38-open-source-and-community/code-of-conduct-and-governance/SKILL.md) | Set up code of conduct, governance, and moderation for communities. |
| [`good-first-issues`](skills/38-open-source-and-community/good-first-issues/SKILL.md) | Create welcoming good-first-issues and onboarding docs for contributors. |
| [`sponsorship-and-funding`](skills/38-open-source-and-community/sponsorship-and-funding/SKILL.md) | Plan open-source funding: sponsors, grants, and dual licensing. |
| [`monorepo-tooling`](skills/38-open-source-and-community/monorepo-tooling/SKILL.md) | Set up monorepos with workspaces, build caching, and shared packages. |
| [`api-docs-generator`](skills/38-open-source-and-community/api-docs-generator/SKILL.md) | Generate API documentation with examples, from OpenAPI or code comments. |

### Legal & Compliance (Lite) (`skills/39-legal-and-compliance-lite/`)

Plain-language orientation to common legal topics. Educational only; not legal advice.

| Skill | What it does |
|---|---|
| [`terms-of-service-drafter`](skills/39-legal-and-compliance-lite/terms-of-service-drafter/SKILL.md) | Draft terms of service outlines for websites and apps with key sections. |
| [`nda-explainer`](skills/39-legal-and-compliance-lite/nda-explainer/SKILL.md) | Explain NDAs: scope, term, exclusions, and red flags. |
| [`freelance-contract-outline`](skills/39-legal-and-compliance-lite/freelance-contract-outline/SKILL.md) | Outline freelance contracts: scope, payment, IP, revisions, and termination. |
| [`trademark-and-copyright-basics`](skills/39-legal-and-compliance-lite/trademark-and-copyright-basics/SKILL.md) | Explain trademark, copyright, and fair-use basics for creators. |
| [`gdpr-cookie-banner`](skills/39-legal-and-compliance-lite/gdpr-cookie-banner/SKILL.md) | Plan cookie consent and tracking disclosures for websites. |
| [`small-claims-guide`](skills/39-legal-and-compliance-lite/small-claims-guide/SKILL.md) | Explain how small claims processes generally work and how to prepare. |
| [`business-structure-overview`](skills/39-legal-and-compliance-lite/business-structure-overview/SKILL.md) | Compare sole proprietorship, LLC, and corporation at a high level. |
| [`accessibility-compliance`](skills/39-legal-and-compliance-lite/accessibility-compliance/SKILL.md) | Explain accessibility compliance expectations (WCAG, ADA, EAA) for digital products. |

### Sports & Game Analysis (`skills/40-sports-and-game-analysis/`)

Strategy, analytics, and improvement in sports, esports, and games.

| Skill | What it does |
|---|---|
| [`chess-improvement`](skills/40-sports-and-game-analysis/chess-improvement/SKILL.md) | Improve at chess: opening principles, tactics, endgames, and game review. |
| [`esports-vod-review`](skills/40-sports-and-game-analysis/esports-vod-review/SKILL.md) | Review gameplay recordings for decision-making, positioning, and mechanics. |
| [`sports-stats-analysis`](skills/40-sports-and-game-analysis/sports-stats-analysis/SKILL.md) | Analyze sports statistics with per-minute rates, efficiency, and context. |
| [`fantasy-sports-strategy`](skills/40-sports-and-game-analysis/fantasy-sports-strategy/SKILL.md) | Build fantasy sports strategy: drafting, waivers, and lineup decisions. |
| [`tournament-organizer`](skills/40-sports-and-game-analysis/tournament-organizer/SKILL.md) | Organize tournaments: brackets, scheduling, rules, and communication. |
| [`game-strategy-analysis`](skills/40-sports-and-game-analysis/game-strategy-analysis/SKILL.md) | Analyze strategy in board games and video games: openings, resources, and tempo. |
| [`speedrun-route-planner`](skills/40-sports-and-game-analysis/speedrun-route-planner/SKILL.md) | Plan speedrun routes: splits, tricks, risk, and practice. |
| [`team-practice-planner`](skills/40-sports-and-game-analysis/team-practice-planner/SKILL.md) | Plan team practices and drills for amateur sports. |

### Unity & Unreal Deep Dives (`skills/41-unity-unreal-deep-dives/`)

Engine-specific techniques beyond the basics.

| Skill | What it does |
|---|---|
| [`unity-ui-toolkit`](skills/41-unity-unreal-deep-dives/unity-ui-toolkit/SKILL.md) | Build Unity UI with UI Toolkit and uGUI: layouts, data binding, and scaling. |
| [`unity-addressables`](skills/41-unity-unreal-deep-dives/unity-addressables/SKILL.md) | Manage assets with Unity Addressables: groups, loading, memory, and updates. |
| [`unity-dots-ecs`](skills/41-unity-unreal-deep-dives/unity-dots-ecs/SKILL.md) | Use Unity DOTS and ECS for high-performance simulation. |
| [`unity-shader-graph`](skills/41-unity-unreal-deep-dives/unity-shader-graph/SKILL.md) | Create effects with Unity Shader Graph and HLSL. |
| [`unity-multiplayer-netcode`](skills/41-unity-unreal-deep-dives/unity-multiplayer-netcode/SKILL.md) | Build multiplayer in Unity with Netcode for GameObjects or Mirror. |
| [`unreal-gameplay-ability-system`](skills/41-unity-unreal-deep-dives/unreal-gameplay-ability-system/SKILL.md) | Implement abilities, effects, and attributes with Unreal's Gameplay Ability System. |
| [`unreal-niagara-vfx`](skills/41-unity-unreal-deep-dives/unreal-niagara-vfx/SKILL.md) | Create Niagara VFX in Unreal: emitters, modules, and optimization. |
| [`unreal-level-streaming`](skills/41-unity-unreal-deep-dives/unreal-level-streaming/SKILL.md) | Use World Partition and level streaming for large Unreal worlds. |
| [`unreal-multiplayer-replication`](skills/41-unity-unreal-deep-dives/unreal-multiplayer-replication/SKILL.md) | Replicate gameplay in Unreal: ownership, RPCs, relevancy, and prediction. |
| [`engine-choice-guide`](skills/41-unity-unreal-deep-dives/engine-choice-guide/SKILL.md) | Choose between Godot, Unity, Unreal, and others for a project. |

### Travel & Languages (`skills/42-travel-and-languages/`)

Planning trips and learning specific languages.

| Skill | What it does |
|---|---|
| [`japan-travel-planner`](skills/42-travel-and-languages/japan-travel-planner/SKILL.md) | Plan Japan trips: regions, rail passes, lodging, food, and etiquette. |
| [`japanese-learning`](skills/42-travel-and-languages/japanese-learning/SKILL.md) | Learn Japanese: kana, kanji, grammar patterns, vocabulary, and immersion. |
| [`spanish-learning`](skills/42-travel-and-languages/spanish-learning/SKILL.md) | Learn Spanish with conjugation, vocabulary, listening, and conversation practice. |
| [`road-trip-planner`](skills/42-travel-and-languages/road-trip-planner/SKILL.md) | Plan road trips: route, stops, budget, and vehicle prep. |
| [`budget-travel-hacks`](skills/42-travel-and-languages/budget-travel-hacks/SKILL.md) | Travel cheaper with flexible dates, hostels, transit, and local food. |
| [`travel-packing-list`](skills/42-travel-and-languages/travel-packing-list/SKILL.md) | Build packing lists by destination, weather, and trip length. |
| [`language-exchange-practice`](skills/42-travel-and-languages/language-exchange-practice/SKILL.md) | Practice languages through roleplay, corrections, and vocabulary drills. |
| [`learn-to-read-faster`](skills/42-travel-and-languages/learn-to-read-faster/SKILL.md) | Improve reading speed and comprehension with practical techniques. |

### Systems & Embedded (`skills/43-systems-and-embedded/`)

Low-level programming, firmware, and performance-critical code.

| Skill | What it does |
|---|---|
| [`rust-systems-programming`](skills/43-systems-and-embedded/rust-systems-programming/SKILL.md) | Write systems code in Rust: traits, error handling, async, FFI, and cargo workflows. |
| [`cpp-memory-and-performance`](skills/43-systems-and-embedded/cpp-memory-and-performance/SKILL.md) | Debug and optimize C++ memory and performance: leaks, cache behavior, sanitizers, and profiling. |
| [`embedded-firmware`](skills/43-systems-and-embedded/embedded-firmware/SKILL.md) | Design embedded firmware: interrupts, timers, state machines, low power, and drivers. |
| [`rtos-and-concurrency`](skills/43-systems-and-embedded/rtos-and-concurrency/SKILL.md) | Use FreeRTOS or Zephyr: tasks, queues, mutexes, and priority pitfalls. |
| [`serial-protocols`](skills/43-systems-and-embedded/serial-protocols/SKILL.md) | Implement and debug I2C, SPI, UART, and CAN communication. |
| [`assembly-and-reverse-reading`](skills/43-systems-and-embedded/assembly-and-reverse-reading/SKILL.md) | Read and write basic assembly and understand compiler output for your own code. |
| [`operating-system-concepts`](skills/43-systems-and-embedded/operating-system-concepts/SKILL.md) | Explain OS concepts: processes, scheduling, memory, filesystems, and syscalls. |
| [`networking-fundamentals`](skills/43-systems-and-embedded/networking-fundamentals/SKILL.md) | Explain networking: TCP/IP, DNS, HTTP, TLS, NAT, and troubleshooting with ping, traceroute, and tcpdump. |
| [`compiler-and-parser-basics`](skills/43-systems-and-embedded/compiler-and-parser-basics/SKILL.md) | Build lexers, parsers, and interpreters for small languages or config formats. |
| [`concurrency-debugging`](skills/43-systems-and-embedded/concurrency-debugging/SKILL.md) | Find and fix race conditions, deadlocks, and thread-safety bugs. |

### Godot Advanced (`skills/44-godot-advanced/`)

Deeper Godot 4 techniques for shipping polished games.

| Skill | What it does |
|---|---|
| [`godot-shaders-visual`](skills/44-godot-advanced/godot-shaders-visual/SKILL.md) | Write Godot 4 canvas_item and spatial shaders: outlines, dissolve, water, toon, and screen effects. |
| [`godot-procedural-worlds`](skills/44-godot-advanced/godot-procedural-worlds/SKILL.md) | Generate Godot worlds with FastNoiseLite, chunking, tilemaps, and seeded determinism. |
| [`godot-mod-support`](skills/44-godot-advanced/godot-mod-support/SKILL.md) | Add mod support to Godot games: PCK loading, resource packs, and safe scripting. |
| [`godot-dialogue-quests`](skills/44-godot-advanced/godot-dialogue-quests/SKILL.md) | Build dialogue and quest systems in Godot with resources, state tracking, and UI. |
| [`godot-cutscenes-timeline`](skills/44-godot-advanced/godot-cutscenes-timeline/SKILL.md) | Create cutscenes with AnimationPlayer, tracks, and camera control. |
| [`godot-accessibility-options`](skills/44-godot-advanced/godot-accessibility-options/SKILL.md) | Add accessibility: remappable controls, text scaling, colorblind modes, and subtitles. |
| [`godot-steam-integration`](skills/44-godot-advanced/godot-steam-integration/SKILL.md) | Integrate Steamworks in Godot using GodotSteam: achievements, cloud saves, and overlay. |
| [`godot-testing-gut`](skills/44-godot-advanced/godot-testing-gut/SKILL.md) | Test Godot code with GUT: unit tests, scene tests, and CI. |

### Power User & Desktop (`skills/45-power-user-and-desktop/`)

Getting more from your computer: terminal, editors, and workflows.

| Skill | What it does |
|---|---|
| [`terminal-productivity`](skills/45-power-user-and-desktop/terminal-productivity/SKILL.md) | Set up a fast terminal workflow: shell config, aliases, fzf, tmux, and dotfiles. |
| [`vim-neovim-guide`](skills/45-power-user-and-desktop/vim-neovim-guide/SKILL.md) | Learn Vim and Neovim: motions, text objects, macros, and a minimal config. |
| [`vscode-setup`](skills/45-power-user-and-desktop/vscode-setup/SKILL.md) | Configure VS Code: extensions, settings, tasks, debugging, and snippets for a language. |
| [`macos-power-user`](skills/45-power-user-and-desktop/macos-power-user/SKILL.md) | Use macOS efficiently: shortcuts, Spotlight, Shortcuts app, automation, and window management. |
| [`keyboard-shortcuts-mastery`](skills/45-power-user-and-desktop/keyboard-shortcuts-mastery/SKILL.md) | Plan learning keyboard shortcuts for your main apps to speed up work. |
| [`file-organization-system`](skills/45-power-user-and-desktop/file-organization-system/SKILL.md) | Create a file and folder organization system with naming, archives, and backups. |

## Structure

```
claude-skills-library/
├── README.md
├── skills-index.json     # machine-readable list of all skills
├── LICENSE
├── CONTRIBUTING.md
├── scripts/
│   ├── install.sh          # install into Claude Code
│   ├── package_all.sh      # build one zip per skill
│   └── validate_skills.py  # lint frontmatter and structure
└── skills/
    ├── 01-decision-making/<skill>/SKILL.md
    ├── 02-coding/<skill>/SKILL.md
    └── ...
```

## Customize

- Edit any `SKILL.md` to fit your style; the `description` field controls when Claude triggers it, so make it specific.
- Add `scripts/`, `references/`, or `assets/` folders inside a skill for bundled resources.
- Run `python3 scripts/validate_skills.py` after changes.

## Notes

- Finance skills are educational, not personalized financial, legal, or tax advice.
- Security skills are defensive only.

## License

MIT. See [LICENSE](LICENSE).
