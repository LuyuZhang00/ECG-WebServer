from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import PatientManage
@admin.register(PatientManage)
class HospitalManage(ImportExportModelAdmin):
    # 设置页面可以展示的字段
    list_display = ('patient_id', 'patient_name','patient_age','patient_sex',
                'patient_department','patient_describe','patient_telephone',
                'patient_photo','create_time','update_time')

    # 默认不配置的话，第一个字段会存在链接到记录编辑页面
    # list_display_links = None
    # list_display_links = ('hospital_name',)
    # 设置过滤选项
    # list_filter = ('JOB_TYPE', 'CREATED_TIME',)
    # 每页显示条目数 缺省值100
    list_per_page = 100
    # show all页面上的model数目，缺省200
    # list_max_show_all = 200
    # 设置可编辑字段 如果设置了可以编辑字段，页面会自动增加保存按钮
    # list_editable = ('hospital_SoftLicense','hospital_SoftLicense_used')
    # 按日期月份筛选 该属性一般不用
    date_hierarchy = 'create_time'
    # 按发布日期降序排序
    ordering = ('-create_time',)
    # 搜索条件设置
    search_fields = ('patient_name',)

    # """
    #   这种禁用编辑链接的放法只是不让它在页面中显示，即把超链接去掉了，
    #   注意：这里建议删除按钮要禁用掉，否则只有拥有view权限的人员依然可以进行删除动作，或者需要进行人员角色判断
    # """
    # def has_add_permission(self, request):
    #     # 禁用添加按钮
    #     return True

    # def has_delete_permission(self, request, obj=None):
    #     # 禁用删除按钮
    #     return False

    # fields 用于控制编辑页面内，需要编辑的字段，逐个显示所有的非AutoField和editable=True
    #        这里可以采用二维元组的方式进行设定对应字段是否在一行显示，可通过 浏览器开发者工具进行查看确认
    # fieldsets 是二维元组列表，用于对编辑页面的布局，与fields属性互斥
    fieldsets = (
        (None, {
            'fields': ('patient_id','patient_name',"patient_department","patient_describe")
        }),
        ('选填字段', {
            'classes': ('wide', 'extrapretty',),
            'fields': ('patient_age','patient_sex','patient_photo','patient_telephone',
              ),
        }),
    )
    save_as_continue = False # 修改完成之后跳转到元素列表页面

    # # 增加自定义按钮
    # actions = ['make_copy', 'custom_button']
    #
    # def custom_button(self, request, queryset):
    #     pass
    #
    # # 显示的文本，与django admin一致
    # custom_button.short_description = '测试按钮'
    # # icon，参考element-ui icon与https://fontawesome.com
    # custom_button.icon = 'fas fa-audio-description'
    #
    # # 指定element-ui的按钮类型，参考https://element.eleme.cn/#/zh-CN/component/button
    # custom_button.type = 'danger'
    #
    # # 给按钮追加自定义的颜色
    # custom_button.style = 'color:black;'
    #
    # def make_copy(self, request, queryset):
    #     pass
    # make_copy.short_description = '复制员工'



    # from django.contrib.admin.templatetags.admin_modify import *
    # from django.contrib.admin.templatetags.admin_modify import submit_row as original_submit_row

    # @register.inclusion_tag('admin/submit_line.html', takes_context=True)
    # def submit_row(context):
    #     ctx = original_submit_row(context)
    #     ctx.update({
    #         'show_save_and_add_another': context.get('show_save_and_add_another', ctx['show_save_and_add_another']),
    #         'show_save_and_continue': context.get('show_save_and_continue', ctx['show_save_and_continue'])
    #     })
    #     return ctx
    # 重写方法屏蔽按钮
    # def change_view(self, request, object_id, form_url='', extra_context=None):
    #     extra_context = extra_context or {}
    #     extra_context['show_save_and_add_another'] = False
    #     extra_context['show_save_and_continue'] = False
    #     return super(PatientManage, self).change_view(request, object_id,
    #         form_url, extra_context=extra_context)

# # 获取登录人员信息，进行填充，需要重写save_model方法,同时记得设定成只读字段
#     def save_model(self, request, obj, form, change):
#         if change: # 判断当前是修改状态还是新增状态
#             obj.update_by = request.user.username
#             obj.save()
#         else:
#             obj.create_by = request.user.username
#             obj.update_by = request.user.username
#             obj.save()
#     readonly_fields = ("create_by", "create_time", "update_by", "update_time")