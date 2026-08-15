# Voice Runtime

A modular real-time voice agent runtime designed to support both **managed realtime infrastructure** such as LiveKit and **custom implementations**.

The goal is to understand and build the core systems behind modern voice agents while keeping the architecture flexible enough for production experimentation.

## Architecture

```text
                    Voice Runtime
                         │
              ┌──────────┴──────────┐
              │                     │
        LiveKit Adapter       Custom Adapter
              │                     │
              └──────────┬──────────┘
                         │
                    Agent Core
                         │
          ┌──────────────┼──────────────┐
          │              │              │
         STT            LLM            TTS
          │              │              │
       Streaming       Tools         Streaming
                         │
                      Memory
                         │
                  Observability
```

## Goals

* Build a real-time voice agent from the ground up.
* Support both LiveKit and custom realtime implementations.
* Understand streaming audio, VAD, turn detection and interruption handling.
* Support pluggable STT, LLM and TTS providers.
* Measure and optimize voice-agent latency.
* Build production-oriented observability and evaluation.
* Keep the core independent from any particular infrastructure provider.

## Planned Features

* [ ] Real-time audio transport
* [ ] LiveKit integration
* [ ] Custom WebSocket transport
* [ ] Streaming STT
* [ ] LLM orchestration
* [ ] Streaming TTS
* [ ] Voice activity detection
* [ ] Turn detection
* [ ] Interruption / barge-in handling
* [ ] Tool calling
* [ ] Conversation state and memory
* [ ] Observability and tracing
* [ ] Latency benchmarking
* [ ] Voice-agent evaluation

## Project Philosophy

**Build first. Understand while building. Replace abstractions when useful.**

Voice Runtime intentionally separates the agent core from infrastructure and model providers. This makes it possible to compare managed solutions with custom implementations without rewriting the entire system.

## Status

🚧 Early development

The initial goal is to build a working MVP and progressively evolve it into a more complete voice-agent runtime.

## License

TBD
