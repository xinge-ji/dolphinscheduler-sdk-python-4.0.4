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

"""Test Task SeaTunnel."""

from unittest.mock import patch

from pydolphinscheduler.tasks.seatunnel import SeaTunnel


def test_seatunnel_get_define():
    """Test task seatunnel function get_define."""
    startup_script = "seatunnel.sh"
    raw_script = """
    env {
        execution.parallelism = 1
    }
    
    source {
        FakeSource {
            result_table_name = "fake"
            field_name = "name,age"
        }
    }
    transform {
        sql {
            sql = "select name,age from fake"
        }
    }
    sink {
        ConsoleSink {}
    }
    """
    use_custom = True
    deploy_mode = "cluster"

    code = 123
    version = 1
    name = "test_seatunnel_get_define"
    expect_task_params = {
        "resourceList": [],
        "localParams": [],
        "startupScript": startup_script,
        "rawScript": raw_script,
        "useCustom": use_custom,
        "deployMode": deploy_mode,
        "dependence": {},
        "conditionResult": {"successNode": [""], "failedNode": [""]},
        "waitStartTimeout": {},
    }
    with patch(
        "pydolphinscheduler.core.task.Task.gen_code_and_version",
        return_value=(code, version),
    ):
        seatunnel = SeaTunnel(name, startup_script, raw_script, use_custom, deploy_mode)
        assert seatunnel.task_params == expect_task_params
