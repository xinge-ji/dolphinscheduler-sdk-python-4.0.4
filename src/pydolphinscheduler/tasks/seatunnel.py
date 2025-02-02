# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

"""Task SeaTunnel."""

from pydolphinscheduler.constants import TaskType
from pydolphinscheduler.core.task import BatchTask


class SeaTunnel(BatchTask):
    """Task SeaTunnel object, declare behavior for SeaTunnel task to dolphinscheduler.
    :param name: task name
    :param zookeeper: SeaTunnel cluster zookeeper address, e.g. 127.0.0.1:2181.
    :param zookeeper_path: SeaTunnel cluster zookeeper path, e.g. /openmldb.
    :param execute_mode: Determine the init mode, offline or online. You can switch it in sql statementself.
    :param sql: SQL statement.
    """

    _task_custom_attr = {
        "startup_script",
        "use_custom",
        "raw_script",
        "deploy_mode",
    }

    def __init__(
        self,
        name: str,
        startup_script: str,
        raw_script: str,
        use_custom: bool,
        deploy_mode: str,
        *args,
        **kwargs,
    ):
        super().__init__(name, TaskType.OPENMLDB, *args, **kwargs)
        self.startup_script = startup_script
        self.raw_script = raw_script
        self.use_custom = use_custom
        self.deploy_mode = deploy_mode
