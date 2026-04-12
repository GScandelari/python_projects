# ============================================================
# advanced/projects/03-pattern-library/solution_pipeline.py
# ============================================================

import functools
import time

# ----------------------------------------------------------
# Decorators
# ----------------------------------------------------------
def timed(func):
    """Decorator: print elapsed time after function completes."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start  = time.perf_counter()
        result = func(*args, **kwargs)
        print(f"  [{func.__name__}] elapsed: {time.perf_counter()-start:.4f}s")
        return result
    return wrapper

def retry(times=3, exceptions=(Exception,)):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last = None
            for attempt in range(1, times + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    last = e
            raise last
        return wrapper
    return decorator


# ----------------------------------------------------------
# Observer / EventEmitter
# ----------------------------------------------------------
class EventEmitter:
    def __init__(self):
        self._listeners = {}

    def on(self, event, callback):
        self._listeners.setdefault(event, []).append(callback)
        return self   # chainable

    def emit(self, event, **data):
        for cb in self._listeners.get(event, []):
            cb(**data)


# ----------------------------------------------------------
# Pipeline stages (generator transformers)
# ----------------------------------------------------------
def filter_stage(predicate):
    """Return a stage that filters items by predicate."""
    def stage(source):
        for item in source:
            if predicate(item):
                yield item
    return stage

def map_stage(transform):
    """Return a stage that transforms every item."""
    def stage(source):
        for item in source:
            yield transform(item)
    return stage

def batch_stage(size):
    """Return a stage that groups items into batches of `size`."""
    def stage(source):
        batch = []
        for item in source:
            batch.append(item)
            if len(batch) == size:
                yield batch
                batch = []
        if batch:
            yield batch
    return stage


# ----------------------------------------------------------
# Pipeline (Builder pattern)
# ----------------------------------------------------------
class PipelineBuilder:
    def __init__(self):
        self._source  = None
        self._stages  = []
        self._sink    = None
        self._emitter = EventEmitter()

    def source(self, gen_func):
        self._source = gen_func
        return self

    def pipe(self, stage):
        self._stages.append(stage)
        return self

    def sink(self, func):
        self._sink = func
        return self

    def on(self, event, callback):
        self._emitter.on(event, callback)
        return self

    def build(self):
        return Pipeline(
            self._source, self._stages, self._sink, self._emitter
        )


class Pipeline:
    def __init__(self, source, stages, sink, emitter):
        self._source  = source
        self._stages  = stages
        self._sink    = sink
        self._emitter = emitter

    def run(self):
        stream = self._source()
        for stage in self._stages:
            stream = stage(stream)

        count = 0
        errors = 0
        for item in stream:
            try:
                if self._sink:
                    self._sink(item)
                self._emitter.emit("item_processed", item=item)
                count += 1
            except Exception as e:
                self._emitter.emit("error", item=item, error=str(e))
                errors += 1

        self._emitter.emit("complete", processed=count, errors=errors)
        return count, errors


# ----------------------------------------------------------
# Demo
# ----------------------------------------------------------
if __name__ == "__main__":
    import random
    random.seed(1)

    def number_source():
        for n in range(1, 21):
            yield n

    pipeline = (PipelineBuilder()
        .source(number_source)
        .pipe(filter_stage(lambda x: x % 2 == 0))
        .pipe(map_stage(lambda x: x ** 2))
        .pipe(batch_stage(3))
        .sink(lambda batch: print(f"  batch → {batch}"))
        .on("item_processed", lambda item: None)
        .on("complete", lambda processed, errors:
            print(f"\n  Done: {processed} batches, {errors} errors"))
        .build()
    )

    print("--- Pipeline demo: even squares in batches of 3 ---")
    pipeline.run()
