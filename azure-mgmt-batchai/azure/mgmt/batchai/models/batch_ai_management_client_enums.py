# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from enum import Enum


class CachingType(Enum):

    none = "none"
    read_only = "readOnly"
    read_write = "readWrite"


class StorageAccountType(Enum):

    standard_lrs = "Standard_LRS"
    premium_lrs = "Premium_LRS"


class FileServerType(Enum):

    nfs = "nfs"
    glusterfs = "glusterfs"


class FileServerProvisioningState(Enum):

    creating = "creating"
    updating = "updating"
    deleting = "deleting"
    succeeded = "succeeded"
    failed = "failed"


class Code(Enum):

    power_state_creating = "PowerState/Creating"
    power_state_running = "PowerState/Running"
    power_state_suspended = "PowerState/Suspended"
    power_state_suspending = "PowerState/Suspending"
    power_state_deleting = "PowerState/Deleting"
    power_state_failed_error_code = "PowerState/Failed/ErrorCode"


class VmPriority(Enum):

    dedicated = "dedicated"
    low_priority = "lowPriority"


class DeallocationOption(Enum):

    requeue = "requeue"
    terminate = "terminate"
    waitforjobcompletion = "waitforjobcompletion"
    unknown = "unknown"


class ProvisioningState(Enum):

    creating = "creating"
    succeeded = "succeeded"
    failed = "failed"
    deleting = "deleting"


class AllocationState(Enum):

    steady = "steady"
    resizing = "resizing"


class OutputType(Enum):

    model = "model"
    logs = "logs"
    summary = "summary"
    custom = "custom"


class ToolType(Enum):

    cntk = "cntk"
    tensorflow = "tensorflow"
    caffe = "caffe"
    caffe2 = "caffe2"
    chainer = "chainer"
    custom = "custom"


class ExecutionState(Enum):

    queued = "queued"
    running = "running"
    terminating = "terminating"
    succeeded = "succeeded"
    failed = "failed"